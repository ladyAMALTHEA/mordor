import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

def get_age(path, channel_dict, channel_list, age_channel='DAPI', TL_channel='TL'):
    czi = czifile.imread(path)
    img=czi.squeeze()

    data = {}
    for channel in channel_list:
        data[channel] = img[channel_dict[channel],...]
    #dimensions of the image
    ydim = img.shape[2]
    xdim = img.shape[3]
    zoom_x1 = round(xdim/2-xdim/5)
    zoom_x2 = round(xdim-(xdim/2-xdim/5))
    zoom_y1 = round(ydim/2-ydim/5)
    zoom_y2 = round(ydim-(ydim/2-ydim/5))

    #output images
    max_projection = data[age_channel].max(0)
    mid_slice =round(img.shape[1] / 2)
    stage_slice = data[age_channel][mid_slice,:,:]
    TL_stage_slice = data[TL_channel][mid_slice,:,:]
    age_zoom_top = max_projection[zoom_y1:zoom_y2,  zoom_x1:zoom_x2]
    age_zoom_mid = stage_slice[zoom_y1:zoom_y2,  zoom_x1:zoom_x2]
    TL_age_zoom_mid = TL_stage_slice[zoom_y1:zoom_y2,  zoom_x1:zoom_x2]


    #to see images
    fig = plt.figure(figsize=(75,75))
    ax=fig.add_subplot(3,2,1)
    plt.imshow(max_projection, cmap='gray', vmin=np.min(max_projection), vmax=np.max(max_projection)-1)
    ax=fig.add_subplot(3,2,2)
    plt.imshow(stage_slice, cmap='gray', vmin=np.min(stage_slice), vmax=np.max(stage_slice)-1)
    ax=fig.add_subplot(3,2,3)
    plt.imshow(age_zoom_top, cmap='gray', vmin=np.min(age_zoom_top), vmax=np.max(age_zoom_top)-1)
    ax=fig.add_subplot(3,2,4)
    plt.imshow(age_zoom_mid, cmap='gray', vmin=np.min(age_zoom_mid), vmax=np.max(age_zoom_mid)-1)
    ax=fig.add_subplot(3,2,5)
    plt.imshow(TL_stage_slice, cmap='gray', vmin=np.min(TL_stage_slice), vmax=np.max(TL_stage_slice)-1)
    ax=fig.add_subplot(3,2,6)
    plt.imshow(TL_age_zoom_mid, cmap='gray', vmin=np.min(TL_age_zoom_mid), vmax=np.max(TL_age_zoom_mid)-1)

    #time to save
    fig.savefig(f"{path[:-4]}_DAPI")

def get_folder_ages(work_dir, channel_dict, channel_list=None, age_channel='DAPI'):
    if channel_list is None:
        channel_list = list(channel_dict.keys())

    for filename in os.listdir(work_dir):
        if filename.endswith(".czi"):
            print(os.path.join(work_dir, filename))
            path = os.path.join(work_dir, filename)
            get_age(path, channel_dict, channel_list, age_channel)
        else:
            continue

if __name__ == '__main__':
    work_dir = '/n/groups/depace/of12/images/CAD_gt/wt_CAD'
    channel_dict = {'DAPI': 0, 'TL':1, 'CAD':2, 'pho':3, 'gt':4}
    channel_list = ['DAPI', 'TL', 'CAD', 'pho', 'gt'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/CAD_gt/pho_CAD'
    channel_dict = {'DAPI': 0, 'TL':1, 'CAD':2, 'pho':3, 'gt':4}
    channel_list = ['DAPI', 'TL', 'CAD', 'pho', 'gt'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/esc_gaps'
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'kr':3, 'hb':4}
    channel_list = ['DAPI', 'TL', 'gt', 'kr', 'hb'] 
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/ez'
    # Gt 488, Ez 546, Kr/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'ez':3, 'kr':4}
    channel_list = ['DAPI', 'TL', 'gt', 'ez', 'kr'] #keep for iteration   
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/sfmbt'
    # Gt 488, Sfmbt 546, Kr/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'sfmbt':3, 'kr':4}
    channel_list = ['DAPI', 'TL', 'gt', 'sfmbt', 'kr'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/psc'
    # Gt 488, Psc 546, Kr/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'psc':3, 'kr':4}
    channel_list = ['DAPI', 'TL', 'gt', 'psc', 'kr'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/gt_hb'
    # Gt 488, Pho 546, Snail/Hb 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'pho':3, 'hb':4}
    channel_list = ['DAPI', 'TL', 'gt', 'pho', 'hb'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/BCD_kr'
    # Snail/Kr 488, BCD 555, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'kr':2, 'BCD':3, 'pho':4}
    channel_list = ['DAPI', 'TL', 'kr', 'BCD', 'pho'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    work_dir = '/n/groups/depace/of12/images/kr_cad'
    # Snail/Kr 488, BCD 555, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'caudal':2, 'pho':3, 'kr':4}
    channel_list = ['DAPI', 'TL', 'kr', 'caudal', 'pho'] #keep for iteration
    get_folder_ages(work_dir, channel_dict, channel_list)

    # work_dir = '/n/groups/depace/of12/images/kni_eve'
    # # eve 488, pho 555, kni/snail 647
    # channel_dict = {'DAPI': 0, 'TL':1, 'eve':2, 'pho':3, 'kni':4}
    # channel_list = ['DAPI', 'TL', 'eve', 'kni', 'pho'] #keep for iteration
    # get_folder_ages(work_dir, channel_dict, channel_list)

    # work_dir = '/n/groups/depace/of12/images/kr_slp1/all_kr_slp'
    # # Slp-1 488, Pho 546, Snail 594, Kr 647
    # channel_dict = {'DAPI': 0, 'TL': 1, 'slp':2, 'pho':3, 'snail':4, 'kr':5,}
    # channel_list = ['DAPI', 'TL', 'slp', 'pho', 'snail', 'kr'] #keep for iteration
    # get_folder_ages(work_dir, channel_dict, channel_list)
