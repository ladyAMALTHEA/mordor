
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

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
