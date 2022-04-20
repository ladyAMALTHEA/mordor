import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

work_dir = '/n/scratch3/users/o/of12/images/kr_slp_pho'
# Slp-1 488, Pho 546, Snail 594, Kr 647
channel_dict = {'DAPI': 0, 'slp':1, 'pho':2, 'snail':3, 'kr':4,}
channel_list = ['DAPI', 'slp', 'pho', 'snail', 'kr'] #keep for iteration

file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
for filename in file_list:
    path = os.path.join(work_dir, filename)
    if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
        data, img = load_data(path, channel_dict, channel_list)
        fig = show_thresh_test(data)
        fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
        plt.close(fig)
