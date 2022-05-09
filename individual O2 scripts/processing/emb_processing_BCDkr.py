import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
 #BCD and Kr data for Pho and WT
    csv_file = 'settings_BCDKr.csv'
    work_dir = '/n/groups/depace/of12/images/BCD_kr'
    # Snail/Kr 488, BCD 555, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'pho':2, 'BCD':3, 'kr':4}
    channel_list = ['DAPI', 'kr', 'BCD', 'pho'] #keep for iteration
    data_channel_list = ['kr', 'BCD', 'pho']
    shape_channel = 'DAPI'
    ap_channel = 'DAPI'
    dv_channel = 'kr'
    z_offset = 3

    database = load_csv_database(os.path.join(work_dir, csv_file))
    all_traces = get_all_traces(database, 
                                data_channel_list, 
                                channel_dict, 
                                channel_list, 
                                work_dir, 
                                dv_channel, 
                                z_offset, 
                                save=True)