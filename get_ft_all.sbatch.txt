#!/bin/bash

#SBATCH -p priority
#SBATCH -t 1-00:00
#SBATCH -c 5
#SBATCH --mem=100G
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -J get_ft_all
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ofoster@g.harvard.edu

python ~/imgproc/scripts/get_ft_gthb.py 
python ~/imgproc/scripts/get_ft_BCDKr.py
python ~/imgproc/scripts/get_ft_ez.py
python ~/imgproc/scripts/get_ft_krslp_wt.py
python ~/imgproc/scripts/get_ft_krslp_pho.py
python ~/imgproc/scripts/get_ft_psc.py
python ~/imgproc/scripts/get_ft_sfmbt.py
