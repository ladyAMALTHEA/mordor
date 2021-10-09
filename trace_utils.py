from imgproc_utils import *
import csv

def load_csv_database(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = {}
        for row in reader:
            database[row['filename']] = row
    return database


def get_all_traces(database, channel_dict, channel_list, work_dir, save=False):
    all_traces = {}
    for filename, info in database.items(): #for each file in the database
        this_dict = {}
        if not info['quality'].upper() == 'GOOD':
            continue
        this_dict['genotype'] = info['genotype']
        this_dict['thresh_method'] = info['thresh_method']
        this_dict['flip'] = info['flip'].upper() == 'TRUE'
        #load the data
        path = os.path.join(work_dir, filename)
        data, _ = load_data(path, channel_dict, channel_list)
        #start getting traces
        
        ...
        
        
        all_traces[filename] = this_dict
    #check quality column
    ...


def get_traces(data,
            flip,
            method='OHTSU', 
            z_plane=None, 
            shape_channel='DAPI', 
            ap_channel='DAPI', 
            bkgd=200):
    if z_plane is None:
        z_plane = data[shape_channel].shape[0] // 2
    z_planes = [z_plane - 1, z_plane, z_plane + 1]

    for z_plane in z_planes:
        for channel, channel_data in data.items():
            ...


def _get_trace(data, method, flip, bkgd):
    ...


def format_trace_datastructure(trace_sets):
    datastructure = {}
    for trace_set in trace_sets:
        ...#organize genotypes