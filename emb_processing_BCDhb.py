import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
    #WBCD and hb data
    csv_file = 'settings_BCDhb.csv'
    work_dir = '/n/groups/depace/of12/images/BCD_hb'
    # BCD 1:100 555, hb/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'BCD':2, 'hb':3}
    channel_list = ['DAPI', 'BCD', 'hb'] #keep for iteration
    data_channel_list = ['BCD', 'hb']
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