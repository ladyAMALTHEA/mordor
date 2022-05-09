#!/bin/bash

#SBATCH -p priority
#SBATCH -t 0-5:00
#SBATCH -c 5
#SBATCH --mem=50G
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -J get_threshAP_krslp
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ofoster@g.harvard.edu

python ~/imgproc/scripts/get_threshAP_krslp_wt.py
python ~/imgproc/scripts/get_threshAP_krslp_pho.py
