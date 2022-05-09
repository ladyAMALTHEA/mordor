#!/bin/bash

#SBATCH -p priority
#SBATCH -t 1-00:00
#SBATCH -c 5
#SBATCH --mem=100G
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -J get_thresh_all
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ofoster@g.harvard.edu


python ~/imgproc/scripts/get_thresh_CAD_pho.py 
python ~/imgproc/scripts/get_thresh_CAD_wt.py 
python ~/imgproc/scripts/get_thresh_esc_gaps.py 
python ~/imgproc/scripts/get_thresh_kr_cad.py 
python ~/imgproc/scripts/get_thresh_kr_slp1.py 
python ~/imgproc/scripts/get_thresh_BCD_kr.py 
##python ~/imgproc/scripts/get_thresh_kni_eve.py 
##python ~/imgproc/scripts/get_thresh_gt_hb.py 

