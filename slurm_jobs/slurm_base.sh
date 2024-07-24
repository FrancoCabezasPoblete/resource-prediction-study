#!/bin/bash
# Job name:
#SBATCH --job-name=resource_prediction_study_usm
#
# Account:
#SBATCH --account=fc_neuronident
#
# Partition:
#SBATCH --partition=partition_name
#
# Wall clock limit:
#SBATCH --time=05:00:00
#
## Command(s) to run:
apptainer run -B /global/home/users/francoale2010/results/<partition>:/results /global/home/users/francoale2010/mycontainer.sif