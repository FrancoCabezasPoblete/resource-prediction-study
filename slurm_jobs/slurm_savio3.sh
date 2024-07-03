#!/bin/bash
# Job name:
#SBATCH --job-name=resource_prediction_study_usm
#
# Account:
#SBATCH --account=fc_neuronident
#
# Partition:
#SBATCH --partition=savio3
#
# Wall clock limit:
#SBATCH --time=00:45:00
#
## Command(s) to run:
apptainer run -B /global/home/users/francoale2010/results/savio3:/results /global/home/users/francoale2010/mycontainer.sif
