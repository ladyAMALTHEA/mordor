#!/bin/bash

#SBATCH -p priority
#SBATCH -t 1-00:00
#SBATCH -c 5
#SBATCH --mem=100G
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -J get_threshAP_all
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ofoster@g.harvard.edu

# python ~/imgproc/scripts/get_threshAP_gthb.py 
#python ~/imgproc/scripts/get_threshAP_BCDKr.py
#python ~/imgproc/scripts/get_threshAP_ez.py
#python ~/imgproc/scripts/get_threshAP_knieve.py
#python ~/imgproc/scripts/get_threshAP_krslp.py
#python ~/imgproc/scripts/get_threshAP_psc.py
#python ~/imgproc/scripts/get_threshAP_sfmbt.py
python ~/imgproc/scripts/threshing/get_thresh_v1/get_threshAP_CAD_wt.py
