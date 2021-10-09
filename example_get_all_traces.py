from typing import cast
from trace_utils import *

csv_file = ''
work_dir = '/Users/robinhood/Dropbox (HMS)/Data/imaging/processing_test'
channel_dict = {'DAPI': 0, 'TL':1, 'gt':2, 'pho':3, 'hb':4}
# bkgd_signal = 200
channel_list = ['DAPI', 'gt', 'pho', 'hb'] #keep for iteration
shape_channel = 'DAPI'
ap_channel = 'DAPI'
dv_channel = 'hb'

database = load_csv_database(csv_file)
get_all_traces(database, save=True)