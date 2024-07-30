#!/bin/bash
# Job name:
#SBATCH --job-name=resource_prediction_study_usm
#
# Account:
#SBATCH --account=fc_neuronident
#
# Partition:
#SBATCH --partition=savio2
#
# Wall clock limit:
#SBATCH --time=06:00:00
#
## Command(s) to run:
apptainer run -B /global/home/users/francoale2010/results/savio2:/results /global/home/users/francoale2010/mycontainer_savio2.sif
