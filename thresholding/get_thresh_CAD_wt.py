
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

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
