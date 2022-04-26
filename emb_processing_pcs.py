import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
    #PSC data
    csv_file = 'settings_psc.csv'
    work_dir = '/n/groups/depace/of12/images/psc'
    # Gt 488, Psc 546, Kr/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'psc':3, 'kr':4}
    channel_list = ['DAPI', 'gt', 'psc', 'kr'] #keep for iteration
    data_channel_list = ['gt', 'kr', 'psc']
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
    
    #Ez data
    csv_file = 'settings_ez.csv'
    work_dir = '/n/groups/depace/of12/images/ez'
    # Gt 488, Ez 546, Kr/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'ez':3, 'kr':4}
    channel_list = ['DAPI', 'gt', 'ez', 'kr'] #keep for iteration
    data_channel_list = ['gt', 'kr', 'ez']
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
    
    # Sfmbt data
    csv_file = 'settings_sfmbt.csv'
    work_dir = '/n/groups/depace/of12/images/sfmbt'
    # Gt 488, Sfmbt 546, Kr/Snail 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'sfmbt':3, 'kr':4}
    channel_list = ['DAPI', 'gt', 'sfmbt', 'kr'] #keep for iteration
    data_channel_list = ['gt', 'kr', 'sfmbt']
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
