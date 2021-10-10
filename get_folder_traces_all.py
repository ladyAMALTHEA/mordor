import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_BCDKr.csv'
work_dir = '/n/scratch3/users/o/of12/images/BCD_kr'
# Snail/Kr 488, BCD 555, Pho 647
channel_dict = {'DAPI': 0, 'TL':1, 'kr':2, 'BCD':3, 'pho':4}
channel_list = ['DAPI', 'kr', 'BCD', 'pho'] #keep for iteration
data_channel_list = ['kr', 'BCD', 'pho']
shape_channel = 'DAPI'
ap_channel = 'DAPI'
dv_channel = 'kr'
z_offset = 3

database = load_csv_database(csv_file)
all_traces = get_all_traces(database, 
                            data_channel_list, 
                            channel_dict, 
                            channel_list, 
                            work_dir, 
                            dv_channel, 
                            z_offset, 
                            save=True)
