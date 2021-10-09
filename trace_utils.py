from imgproc_utils import *
import csv

def load_csv_database(filename):
    #check quality column
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        database = {}
        for row in reader:
            database[row['filename']] = row

    ...



def get_all_traces(database):
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
