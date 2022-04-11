import math
import matplotlib.pyplot as plt
import numpy as np

import czifile
# from pathlib import Path
import os
from skimage import morphology, exposure, filters
# from skimage.feature import canny
from skimage.measure import regionprops, regionprops_table, label
from scipy import ndimage, misc

def get_thresholded(data, method='OHTSU', shape_channel='DAPI', z_plane=None, bkgd=200):
    if method.upper() == 'OHTSU':
        ## THRESHOLD OHTSU
        zshape = data[shape_channel].max(0)
        bkgd = filters.threshold_otsu(zshape)
        max_signal = np.max(zshape)-1
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        zshape = filters.threshold_sauvola(zshape)
        zshape = morphology.binary_closing(zshape)
    elif method.upper() == 'GAMMA':
        # GAMMA THRESHOLD
        if z_plane is None:
            z_plane = data[shape_channel].shape[0] // 2
        zshape = data[shape_channel][z_plane,:,:]

        max_signal = np.max(zshape)-1#np.quantile(zshape, 0.7)
        zshape = exposure.adjust_gamma(zshape)
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        zshape = morphology.binary_closing(zshape)
    elif method.upper() == 'DILL':
        # THRESHOLD DILATION
        zshape = data[shape_channel].max(0)
        zshape = exposure.adjust_gamma(zshape)
        max_signal = np.max(zshape)-1
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        footprint=morphology.disk(25) # size hard coded
        zshape = morphology.binary_dilation(zshape, footprint)
    elif method.upper() == 'GAMMA_V2':
        # GAMMA THRESHOLD
        if z_plane is None:
            z_plane = data[shape_channel].shape[0] // 2
        zshape = data[shape_channel][z_plane,:,:]
        bkgd = filters.threshold_otsu(zshape)
        max_signal = np.max(zshape)-1#np.quantile(zshape, 0.7)
        zshape = exposure.adjust_gamma(zshape)
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        zshape = morphology.binary_closing(zshape)
    elif method.upper() == 'JEFE_1':
        #JEFE_1 THRESHOLD
        footprint=morphology.disk(15)
        zshape = data[shape_channel].std(0)
        bkgd = zshape.min()
        zshape -= bkgd
        zshape[zshape < 0] = 0
        bkgd = filters.threshold_otsu(zshape)
        zshape -= bkgd
        zshape[zshape < 0] = 0
        zshape = exposure.adjust_gamma(zshape)
        bkgd = filters.threshold_otsu(zshape)
        max_signal = np.max(zshape)-1
        zshape = filters.threshold_sauvola(zshape)
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        zshape = morphology.binary_erosion(zshape, footprint)
        zshape = morphology.binary_closing(zshape)
        zshape = morphology.binary_dilation(zshape, footprint)
        zshape = morphology.binary_closing(zshape)
        zshape = morphology.binary_erosion(zshape, footprint)
    elif method.upper() == 'JEFE_2':
        #JEFE_2 THRESHOLD
        zshape = data[shape_channel].std(0)
        bkgd = zshape.min()
        zshape -= bkgd
        zshape[zshape < 0] = 0
        bkgd = filters.threshold_otsu(zshape)
        zshape -= bkgd
        zshape[zshape < 0] = 0
        zshape = exposure.adjust_gamma(zshape)
        bkgd = filters.threshold_otsu(np.nanquantile(zshape.flatten(), 0.75))
        max_signal = np.max(zshape)-1
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        zshape = filters.threshold_sauvola(zshape)#,r=bkgd)
        zshape = morphology.binary_closing(zshape)
        footprint=morphology.disk(25)
        zshape = morphology.binary_dilation(zshape, footprint)
        zshape = morphology.binary_closing(zshape)
        zshape = morphology.binary_erosion(zshape, footprint)
    elif method.upper() == 'JEFE_3':
        # JEFE_3 THRESHOLD
        footprint=morphology.disk(25)
        zshape = data[shape_channel].std(0)
        bkgd = zshape.min()
        zshape -= bkgd
        zshape[zshape < 0] = 0
        bkgd = filters.threshold_otsu(zshape)
        zshape -= bkgd
        zshape[zshape < 0] = 0
        zshape = exposure.adjust_gamma(zshape)
        bkgd = filters.threshold_otsu(np.nanquantile(zshape.flatten(), 0.7))
        max_signal = np.max(zshape)-1
        zshape = filters.apply_hysteresis_threshold(zshape, bkgd, max_signal)
        zshape = filters.threshold_sauvola(zshape)
        zshape = morphology.binary_closing(zshape)
        zshape = morphology.binary_dilation(zshape, footprint)
        zshape = morphology.binary_closing(zshape)
        zshape = morphology.binary_erosion(zshape, footprint)
    else:
        #load custom mask from filename in "method" variable


    return zshape

def get_orientation(data, method='OHTSU', shape_channel='DAPI', ap_channel='DAPI', z_plane=None, bkgd=200):
    #get thresholded
    zshape = get_thresholded(data, method, shape_channel, z_plane, bkgd)

    max_AP = data[ap_channel].max(0) # this will be how to pick AP axis
    
    #get_dimensions
    # emb_label= label(zshape.astype(np.uint8))
    emb_regions = regionprops(zshape.astype(np.uint8))
    areas = [emb['area'] for emb in emb_regions]
    props = emb_regions[np.argmax(areas)]

    y0, x0 = props.centroid
    orientation = props.orientation
    # long_axis = props.major_axis_length
    # short_axis = props.minor_axis_length
    # minr, minc, maxr, maxc = props.bbox
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

    rotation_axis = 90 - (orientation * 180/math.pi)
    rotated_AP = ndimage.rotate(max_AP, rotation_axis)
    rotated_AP = exposure.adjust_gamma(rotated_AP)
    return zshape, rotation_axis, rotated_AP, xs, ys


def show_orientation(zshape, rotated_AP, xs, ys, filename=None, path=None):
    fig, ax = plt.subplots(1,2, figsize=(25,25))
    ax[0].imshow(zshape, cmap=plt.cm.gray)
    ax[0].plot((xs[3], xs[1]), (ys[3], ys[1]), '-y', linewidth=10) #minor axis line
    ax[0].plot((xs[4], xs[2]), (ys[4], ys[2]), '-m', linewidth=10) #major axis line
    ax[0].plot(xs[0], ys[0], '.g', markersize=25)

    ax[1].imshow(rotated_AP, cmap=plt.cm.gray)

        #time to save
    if filename is not None:
        if path is not None:
            if path[-4:] == '.czi':
                os.makedirs(path[:-4], exist_ok=True)
                filepath = f"{path[:-4]}_APcheck"
            else:
                os.makedirs(path, exist_ok=True)
                filepath = os.path.join(path, f"{filename[:-4]}_APcheck")
            fig.savefig(filepath)
        else:
            fig.savefig(f"{filename[:-4]}_APcheck")
    return fig


def show_thresh_test(data, 
                    methods_list=['OHTSU', 'GAMMA', 'DILL', 'JEFE_1', 'JEFE_2', 'JEFE_3'], 
                    shape_channel='DAPI', 
                    ap_channel='DAPI', 
                    z_plane=None, 
                    bkgd=200):
    fig, axs = plt.subplots(len(methods_list), 2, figsize=(10, 5*len(methods_list)))
    for i, method in enumerate(methods_list):
        zshape, _, rotated_AP, xs, ys = get_orientation(data, method, shape_channel, ap_channel, z_plane, bkgd)
        axs[i, 0].imshow(zshape, cmap=plt.cm.gray)
        axs[i, 0].plot((xs[3], xs[1]), (ys[3], ys[1]), '-y', linewidth=7) #minor axis line
        axs[i, 0].plot((xs[4], xs[2]), (ys[4], ys[2]), '-m', linewidth=7) #major axis line
        axs[i, 0].plot(xs[0], ys[0], '.g', markersize=15)
        axs[i, 0].set_title(f'{method}: masked')
        axs[i, 0].set_xticks([])
        axs[i, 0].set_yticks([])
        axs[i, 1].imshow(rotated_AP, cmap=plt.cm.gray)
        axs[i, 1].set_title(f'{method}: rotated')
        axs[i, 1].set_xticks([])
        axs[i, 1].set_yticks([])

    return fig

def load_data(path, channel_dict, channel_list):
    czi = czifile.imread(path)
    img=czi.squeeze()
    data = {}
    for channel in channel_list:
        data[channel] = img[channel_dict[channel],...]
    
    return data, img


# def get_oriented_plane(data, z_plane, rotation_axis, flip_hor=False):
#     output = {}
#     for key, value in data.items():

