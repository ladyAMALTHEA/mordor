
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

if __name__ == '__main__':
    ## BCD_Kr
    work_dir = '/n/groups/depace/of12/images/BCD_kr'
    # Snail/Kr 488, BCD 555, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'kr':2, 'BCD':3, 'pho':4}
    channel_list = ['DAPI', 'kr', 'BCD', 'pho'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)


    #gt_hb
    work_dir = '/n/groups/depace/of12/images/gt_hb'
    # Gt 488, Pho 546, Snail/Hb 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'pho':3, 'hb':4}
    channel_list = ['DAPI', 'gt', 'pho', 'hb'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## kni_eve
    work_dir = '/n/groups/depace/of12/images/kni_eve'
    # Eve 488, Kni/Snail 546, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'eve':2, 'kni':3, 'pho':4}
    channel_list = ['DAPI', 'eve', 'kni', 'pho'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## kr_slp_all
    work_dir = '/n/groups/depace/of12/images/kr_slp1/all_kr_slp'
    # Slp-1 488, Pho 546, Snail 594, Kr 647
    channel_dict = {'DAPI': 0, 'TL':1, 'slp':2, 'pho':3, 'snail':4, 'kr':5}
    channel_list = ['DAPI', 'slp', 'pho', 'snail', 'kr'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## esc gaps
    work_dir = '/n/groups/depace/of12/images/esc_gaps'
    # gt 488, kr/snail 546, hb 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'kr':3, 'hb':4}
    channel_list = ['DAPI', 'gt', 'kr', 'hb'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## caudal_wt
    work_dir = '/n/groups/depace/of12/images/CAD_gt/wt_CAD'
    # Gt/Snail 647, Caudal 546
    channel_dict = {'DAPI': 0, 'TL':1, 'CAD':2, 'pho':3, 'gt':4}
    channel_list = ['DAPI', 'CAD', 'gt'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## caudal_pho
    work_dir = '/n/groups/depace/of12/images/CAD_gt/pho_CAD'
    # Gt/Snail 647, Caudal 546
    channel_dict = {'DAPI': 0, 'TL':1, 'CAD':2, 'pho':3, 'gt':4}
    channel_list = ['DAPI', 'CAD', 'gt'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## caudal and kruppel
    work_dir = '/n/groups/depace/of12/images/kr_cad'
    # Gt/Snail 647, Caudal 546
    channel_dict = {'DAPI': 0, 'TL':1, 'cad':2, 'pho':3, 'kr':4}
    channel_list = ['DAPI', 'cad', 'kr'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)

    ## knirps and eve
    work_dir = '/n/groups/depace/of12/images/CAD_gt/pho_CAD'
    # Gt/Snail 647, Caudal 546
    channel_dict = {'DAPI': 0, 'TL':1, 'eve':2, 'pho':3, 'kni':4}
    channel_list = ['DAPI', 'eve', 'kni'] #keep for iteration

    file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
    for filename in file_list:
        path = os.path.join(work_dir, filename)
        if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
            data, img = load_data(path, channel_dict, channel_list)
            fig = show_thresh_test(data)
            fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
            plt.close(fig)