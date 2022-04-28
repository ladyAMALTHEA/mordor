import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
    #WT CAD data
    csv_file = 'settings_CAD_wt_nogt.csv'
    work_dir = '/n/groups/depace/of12/images/CAD_gt/wt_CAD'
    # Pho 488, CAD 555, giant/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'CAD':3, 'pho':2, 'gt':4}
    channel_list = ['DAPI', 'CAD', 'pho', 'gt'] #keep for iteration
    data_channel_list = ['CAD', 'pho']
    shape_channel = 'DAPI'
    ap_channel = 'DAPI'
    dv_channel = 'gt'
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
    
    #Pho CAD data
    csv_file = 'settings_CADgt.csv'
    work_dir = '/n/groups/depace/of12/images/CAD_gt/CADgt'
    # Pho 488, CAD 555, giant/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'CAD':3, 'pho':2, 'gt':4}
    channel_list = ['DAPI', 'CAD', 'pho', 'gt'] #keep for iteration
    data_channel_list = ['CAD', 'pho', 'gt']
    shape_channel = 'DAPI'
    ap_channel = 'DAPI'
    dv_channel = 'gt'
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
    
   