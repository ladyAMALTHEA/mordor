## BCD_Kr
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *

work_dir = '/n/scratch3/users/o/of12/images/BCD_kr'
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
