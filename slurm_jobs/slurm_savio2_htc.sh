#!/bin/bash
# Job name:
#SBATCH --job-name=resource_prediction_study_usm
#
# Account:
#SBATCH --account=fc_neuronident
#
# Partition:
#SBATCH --partition=savio2_htc
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
# Wall clock limit:
#SBATCH --time=05:00:00
#
## Command(s) to run:
apptainer run -B /global/home/users/francoale2010/results/savio2_htc:/results /global/home/users/francoale2010/mycontainer.sif
