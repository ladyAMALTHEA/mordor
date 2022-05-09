import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
    csv_file = 'settings_krcad.csv'
    work_dir = '/n/groups/depace/of12/images/kr_cad'
    # Snail/Kr 488, BCD 555, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'caudal':2, 'pho':3, 'kr':4}
    channel_list = ['DAPI', 'kr', 'caudal', 'pho'] #keep for iteration
    data_channel_list = ['kr', 'caudal', 'pho']
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