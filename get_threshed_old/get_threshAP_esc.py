import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

work_dir = '/n/groups/depace/of12/images/esc'
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
