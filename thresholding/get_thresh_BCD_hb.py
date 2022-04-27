import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

## BCD_Kr
work_dir = '/n/groups/depace/of12/images/BCD_hb'
# Snail/Kr 488, BCD 555, Pho 647
channel_dict = {'DAPI': 0, 'TL':1, 'BCD':2, 'hb':3}
channel_list = ['DAPI', 'BCD', 'hb'] #keep for iteration

file_list = [file for file in os.listdir(work_dir) if file[-4:] == '.czi']
for filename in file_list:
    path = os.path.join(work_dir, filename)
    if not os.path.exists(os.path.join(work_dir, f"{filename[:-4]}_threshAP.png")):
        data, img = load_data(path, channel_dict, channel_list)
        fig = show_thresh_test(data)
        fig.savefig(os.path.join(work_dir, f"{filename[:-4]}_threshAP"))
        plt.close(fig)