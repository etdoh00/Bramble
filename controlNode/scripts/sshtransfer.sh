#!/bin/bash

# loop through nodes p0 to p9
for i in {0..9}; do
    # check if current node is not the local node
    if [ "$i" != "$SLURM_NODEID" ]; then
        # copy ssh key to current node
        ssh-copy-id "master@p$i"
    fi
done

