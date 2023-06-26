#!/bin/bash
cd $SLURM_SUBMIT_DIR

#printing first node to react
echo "Master node: $(hostname)"

#run using mpi - will auto detect resources from slurm
mpirun a.out
