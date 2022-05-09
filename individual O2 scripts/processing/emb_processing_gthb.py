import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
    # Giant and Hunchback Data
    csv_file = 'settings_gthb.csv'
    work_dir = '/n/groups/depace/of12/images/gt_hb'
    # Gt 488, Pho 546, Snail/Hb 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'pho':3, 'hb':4}
    channel_list = ['DAPI', 'gt', 'pho', 'hb'] #keep for iteration
    data_channel_list = ['gt', 'hb', 'pho']
    shape_channel = 'DAPI'
    ap_channel = 'DAPI'
    dv_channel = 'hb'
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
