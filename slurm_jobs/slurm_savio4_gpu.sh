#!/bin/bash
# Job name:
#SBATCH --job-name=resource_prediction_study_usm
#
# Account:
#SBATCH --account=fc_neuronident
#
# Partition:
#SBATCH --partition=savio4_gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
# Wall clock limit:
#SBATCH --time=00:15:00
#
## Command(s) to run:
apptainer run -B /global/home/users/francoale2010/results/savio4_gpu:/results /global/home/users/francoale2010/mycontainer.sif
