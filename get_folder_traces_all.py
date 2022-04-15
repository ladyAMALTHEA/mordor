##BCD_Kr
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_BCDKr.csv'
work_dir = '/n/scratch3/users/o/of12/images/BCD_kr'
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

##gt_hb
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_gthb.csv'
work_dir = '/n/scratch3/users/o/of12/images/gt_hb'
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


##kr_slp_wt
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_krslp_wt.csv'
work_dir = '/n/scratch3/users/o/of12/images/kr_slp_wt'
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


##kr_slp_pho
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_krslp_pho.csv'
work_dir = '/n/scratch3/users/o/of12/images/kr_slp_pho'
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


##psc
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_psc.csv'
work_dir = '/n/scratch3/users/o/of12/images/psc'
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


##sfmbt
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_sfmbt.csv'
work_dir = '/n/scratch3/users/o/of12/images/sfmbt'
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

##ez
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_ez.csv'
work_dir = '/n/scratch3/users/o/of12/images/ez'
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

##esc
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_esc.csv'
work_dir = '/n/groups/depace/of12/images/esc'
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


##CAD pho
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_CAD_pho.csv'
work_dir = '/n/groups/depace/of12/images/CAD_gt/pho_CAD'
# Gt 488, Ez 546, Kr/Snail 647
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


##CAD_wt
import sys
sys.path.append('/home/of12/imgproc/scripts')
from imgproc_utils import *
from typing import cast
from trace_utils import *

csv_file = 'settings_CAD_wt.csv'
work_dir = '/n/groups/depace/of12/images/CAD_gt/wt_CAD'
# Gt 488, Ez 546, Kr/Snail 647
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