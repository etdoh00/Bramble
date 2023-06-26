#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --partition=MellaMini
cd $SLURM_SUBMIT_DIR
mkdir plots
R --vanilla -f gen.R --args "plot$SLURM_ARRAY_TASK_ID"
