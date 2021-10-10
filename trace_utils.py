from imgproc_utils import *
import csv
from skimage.feature import canny
import scipy.stats as stats
import json

def load_csv_database(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = {}
        for row in reader:
            database[row['filename']] = row
    return database


def get_all_traces(database, data_channel_list, channel_dict, channel_list, work_dir, dv_channel, z_offset=3, save=False):
    save_name = None
    all_traces = {}
    for filename, info in database.items(): #for each file in the database
        this_dict = {}
        if not info['quality'].upper() == 'GOOD':
            continue
        this_dict['genotype'] = info['genotype']
        thresh_method = info['thresh_method']
        flip = info['flip'].upper() == 'TRUE'
        #load the data
        path = os.path.join(work_dir, filename) + '.czi'
        data, _ = load_data(path, channel_dict, channel_list)
        #start getting traces
        this_dict['traces'], qc_imgs = get_traces(data, data_channel_list, flip, thresh_method, dv_channel, z_offset)
        if save:
            save_name = f'{path[:-4]}_qcFig'
            make_qc_figs(qc_imgs, this_dict['traces'], save_name)
        all_traces[filename] = this_dict
    if save:
        with open("all_traces.json", "w") as outfile:
            json.dump(all_traces, outfile)
    return all_traces


def get_traces(data,
            flip,
            data_channel_list,
            method='OHTSU', 
            dv_channel='kr', 
            shape_channel='DAPI', 
            ap_channel='DAPI', 
            z_plane=None, 
            bkgd=200,
            z_offset=3):
    if z_plane is None:
        z_plane = data[shape_channel].shape[0] // 2
    z_planes = [z_plane - z_offset, z_plane, z_plane + z_offset]

    #get orientation
    zshape, rotation_axis, _, _, _ = get_orientation(data, method, shape_channel, ap_channel, z_plane, bkgd)
    rot_zshape, rot_xs, rot_ys = orient_mask(zshape, rotation_axis, flip, bkgd)
    dv_divide, im_filled = make_mask(rot_zshape, rot_xs, rot_ys)
    rotated_zdv = orient(data[dv_channel][z_plane,:,:], rotation_axis, flip)
    dorsal_mask, dorsal, ventral = get_dv(dv_divide, rotated_zdv, bkgd)

    qc_imgs = {}
    qc_imgs['emb_mask'] = im_filled
    qc_imgs['dv_divide'] = dv_divide
    qc_imgs['dorsal_check'] = dorsal
    qc_imgs['ventral_check'] = ventral
    traces = {}
    for channel in data_channel_list:
        channel_data = data[channel]
        these_traces = []
        these_maskeds = []
        for z in z_planes:
            rotated = orient(channel_data[z,:,:], rotation_axis, flip)
            trace, masked = get_trace(rotated, dorsal_mask)
            these_traces.append(trace)
            these_maskeds.append(masked)
        traces[channel] = these_traces
        qc_imgs[channel] = these_maskeds

    return traces, qc_imgs

def get_trace(zplane, dorsal_mask, length=100):
    masked_zplane = zplane * dorsal_mask
    sum_trace = masked_zplane.sum(axis=0)
    mask_sum = dorsal_mask.sum(axis=0)
    mean_trace = sum_trace / mask_sum
    trace = mean_trace[mask_sum>0]
    inds = np.arange(trace.shape[0])
    standard_trace, _, _ = stats.binned_statistic(inds, trace, bins=length)
    return standard_trace, masked_zplane

def make_mask(zshape, xs, ys):
    structure = np.ones((3, 3))
    im_filled = ndimage.binary_fill_holes(zshape, structure)
    edge_mask = canny(im_filled)
    footprint = morphology.disk(25)
    edge_mask = morphology.binary_dilation(edge_mask, footprint)
    knife = make_knife(zshape.shape, xs, ys)
    zorro = im_filled*edge_mask # slices off all the extra in edge_mask to make a mask of the area of interest in the embryo
    dv_divide = np.invert(knife) * zorro 

    return dv_divide, im_filled

def make_knife(dims, xs, ys):
    major_axis_line = np.zeros(dims, dtype=bool)

    m_major = (ys[2] - ys[0]) / (xs[2] - xs[0])
    b_major = (ys[2] - (m_major * xs[2]))

    # major axis loop
    major_inds = [] # list
    for x in range(major_axis_line.shape[0]): # this would work even if not horizontal
        y = ((m_major * x) + b_major)
        if y < major_axis_line.shape[0] and y >= 0:
            major_axis_line[int(y),int(x)] = True
            major_inds.append([int(y), int(x)])

    footprint=morphology.disk(10)
    major_axis_knife = morphology.binary_dilation(major_axis_line, footprint)
    return major_axis_knife
    
def get_dv(dv_divide, rotated_zdv, bkgd=200):
    dv_label = label(dv_divide)
    dv_regions = regionprops(dv_label)

    rotated_zdv = exposure.adjust_gamma(rotated_zdv) #normalize for better detection
    # rotated_zdv = filters.apply_hysteresis_threshold(rotated_zdv, bkgd, np.max(rotated_zdv)-1)

    blank = np.zeros(rotated_zdv.shape, dtype=bool)
    sideA = blank.copy()
    bbox = dv_regions[0].bbox
    sideA[bbox[0]:bbox[2], bbox[1]:bbox[3]] = dv_regions[0].image

    sideB = blank.copy()
    bbox = dv_regions[1].bbox
    sideB[bbox[0]:bbox[2], bbox[1]:bbox[3]] = dv_regions[1].image

    # use the two sides and mask the snail hysterics image
    decide_A =  rotated_zdv*sideA
    decide_B =  rotated_zdv*sideB

    # decision point for the DV axis
    if np.sum(decide_A) > np.sum(decide_B):
        dorsal_mask = sideB
        dorsal = decide_B
        ventral = decide_A
    else:
        dorsal_mask = sideA
        dorsal = decide_A
        ventral = decide_B
    return dorsal_mask, dorsal, ventral

def orient(zplane, rotation_axis, flip):
    rotated = ndimage.rotate(zplane, rotation_axis, reshape=True)
    if flip:
        rotated= np.fliplr(rotated)
    return rotated

def orient_mask(zshape, rotation_axis, flip, bkgd=200):
    rotated = ndimage.rotate(zshape, rotation_axis, reshape=True)
    if flip:
        rotated= np.fliplr(rotated)
    
    rotated = exposure.adjust_gamma(rotated)
    rotated = filters.apply_hysteresis_threshold(rotated, bkgd, np.max(rotated)-1)
    rotated = morphology.binary_closing(rotated)
    rotated = canny(rotated, sigma=2.0, low_threshold=0.55, high_threshold=0.8) 
    rotated = morphology.binary_dilation(rotated) # fills a hole in edges
    structure = np.ones((3, 3))
    rotated = ndimage.binary_fill_holes(rotated, structure)

    emb_regions = regionprops(rotated.astype(np.uint8))
    areas = [emb['area'] for emb in emb_regions]
    props = emb_regions[np.argmax(areas)]

    y0, x0 = props.centroid
    orientation = props.orientation
    ys = [y0]
    xs = [x0]
    xs.append(x0 + math.cos(orientation) * 0.5 * props.minor_axis_length) #top
    ys.append(y0 - math.sin(orientation) * 0.5 * props.minor_axis_length)
    xs.append(x0 - math.sin(orientation) * 0.5 * props.major_axis_length)
    ys.append(y0 - math.cos(orientation) * 0.5 * props.major_axis_length)
    xs.append(x0 - math.cos(orientation) * 0.5 * props.minor_axis_length) #bottom
    ys.append(y0 + math.sin(orientation) * 0.5 * props.minor_axis_length)            
    xs.append(x0 + math.sin(orientation) * 0.5 * props.major_axis_length)
    ys.append(y0 + math.cos(orientation) * 0.5 * props.major_axis_length)

    return rotated, xs, ys

def make_qc_figs(imgs, traces, save_name=None):
    fig, axs = plt.subplots(2 + len(traces), 2, figsize=(20, 20 + 10*len(traces)))
    imshow(imgs['emb_mask'], axs[0,0], 'Embryo Mask')
    imshow(imgs['dv_divide'], axs[0,1], 'Dorsal/Ventral Masks')
    imshow(imgs['dorsal_check'], axs[1,0], 'Dorsal Check')
    imshow(imgs['ventral_check'], axs[1,1], 'Ventral Check')
    for i, (channel, channel_traces) in enumerate(traces.items()):
        mean = np.array(channel_traces).mean(0)
        error = np.array(channel_traces).std(0)
        axs[2+i, 0].fill_between(np.arange(mean.shape[0]), mean-error, mean+error, alpha=0.5, linewidth=0)
        axs[2+i, 0].plot(mean)
        axs[2+i, 0].set_title(f'{channel} Mean Trace (w/ Std)')

        imshow(imgs[channel][1], axs[2+i, 1], f'{channel} Check')
    if save_name is not None:
        fig.savefig(save_name)

def format_trace_datastructure(trace_sets, excluded=None):
    datastructure = {}
    for trace_set in trace_sets:
        for filename, file_data in trace_set.items():
            if excluded is not None and filename in excluded:
                continue
            genotype = file_data['genotype']
            if genotype not in datastructure.keys():
                datastructure[genotype] = {}
            for gene, traces in file_data['traces'].items():
                if gene not in datastructure[genotype].keys():
                    datastructure[genotype][gene] = np.expand_dims(np.array(traces), 0) # [embryo, z_plane, trace] -> i.e. [# of embryos, 3, 100]
                else:
                    datastructure[genotype][gene] = np.append(datastructure[genotype][gene], np.array(traces), 0)
    return datastructure

def imshow(img, ax, title):
    ax.imshow(img, cmap=plt.cm.gray)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])