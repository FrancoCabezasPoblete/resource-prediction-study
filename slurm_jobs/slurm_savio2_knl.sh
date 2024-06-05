#!/bin/bash
# Job name:
#SBATCH --job-name=resource_prediction_study_usm
#
# Account:
#SBATCH --account=fc_neuronident
#
# Partition:
#SBATCH --partition=savio2_knl
#
# Wall clock limit:
#SBATCH --time=00:15:00
#
## Command(s) to run:
apptainer run -B /global/home/users/francoale2010/results/savio2_knl:/results /global/home/users/francoale2010/mycontainer.sif
