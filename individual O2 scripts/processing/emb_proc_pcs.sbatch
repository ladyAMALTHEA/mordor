#!/bin/bash

#SBATCH -p priority
#SBATCH -t 1-00:00
#SBATCH -c 5
#SBATCH --mem=50G
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -J get_ft_all
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ofoster@g.harvard.edu

python ~/imgproc/scripts/emb_processing_pcs.py 
