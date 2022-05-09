from typing import cast
from trace_utils import *

csv_file = 'sumthing.csv'
work_dir = '/Users/robinhood/Dropbox (HMS)/Data/imaging/processing_test'
channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'pho':3, 'hb':4}
# bkgd_signal = 200
channel_list = ['DAPI', 'gt', 'pho', 'hb'] #keep for iteration
data_channel_list = ['gt', 'pho', 'hb']
shape_channel = 'DAPI'
ap_channel = 'DAPI'
dv_channel = 'hb'
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

