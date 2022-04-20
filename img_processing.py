import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *


if __name__ == '__main__':
    #WT CAD data
    csv_file = 'settings_CAD_wt.csv'
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
    csv_file = 'settings_CAD_pho.csv'
    work_dir = '/n/groups/depace/of12/images/CAD_gt/pho_CAD'
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
    
    # Extra Sex combs gap gene data
    csv_file = 'settings_esc_gaps.csv'
    work_dir = '/n/groups/depace/of12/images/esc_gaps'
    # Gt 488, Kr/Snail 546, Hb 647
    channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'kr':3, 'hb':4}
    channel_list = ['DAPI', 'gt', 'kr', 'hb'] #keep for iteration
    data_channel_list = ['gt', 'kr', 'hb']
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
    
    # Pho Kr and Slp1 Data
    csv_file = 'settings_krslp_pho.csv'
    work_dir = '/n/groups/depace/of12/images/kr_slp_pho'
    # Slp-1 488, Pho 546, Snail 594, Kr 647
    channel_dict = {'DAPI': 0, 'slp':1, 'pho':2, 'snail':3, 'kr':4,}
    channel_list = ['DAPI', 'slp', 'pho', 'snail', 'kr'] #keep for iteration
    data_channel_list = ['slp', 'kr', 'pho']
    shape_channel = 'DAPI'
    ap_channel = 'DAPI'
    dv_channel = 'snail'
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
    
    #WT Kr and slp1 data
    csv_file = 'settings_krslp_wt.csv'
    work_dir = '/n/groups/depace/of12/images/kr_slp_wt'
    # Slp-1 488, Pho 546, Snail 594, Kr 647
    channel_dict = {'DAPI': 0, 'TL':1, 'slp':2, 'pho':3, 'snail':4, 'kr':5}
    channel_list = ['DAPI', 'slp', 'pho', 'snail', 'kr'] #keep for iteration
    data_channel_list = ['slp', 'kr', 'pho']
    shape_channel = 'DAPI'
    ap_channel = 'DAPI'
    dv_channel = 'snail'
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

    
    #BCD and Kr data for Pho and WT
    csv_file = 'settings_BCDKr.csv'
    work_dir = '/n/groups/depace/of12/images/BCD_kr'
    # Snail/Kr 488, BCD 555, Pho 647
    channel_dict = {'DAPI': 0, 'TL':1, 'kr':2, 'BCD':3, 'pho':4}
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