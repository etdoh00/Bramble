# Bramble
This is the core of my raspberry Pi Cluster. The cluster consisted of 10 Raspberry Pi's (2 x 3b+. 8x Zero W). It reflects the concepts of HPC.

All Pi's were assigned an IP address statically as if they were to be dynamically, it would make the configuration almost impossible. This can be seen in the config file.
The network was provided by bridging the ethernet's from the 3b+ nodes to the Zero W's by the presence of the "ClusterHAT" which established a USB connection.

To reflect the concepts of high performance computing there were 3 overlays installed: 
----> MPI
----> SLURM
----> K3s

I chose MPI as it is the most primitive of all, and allows for an easy setup. It highlights the basic functionality of how a HPC can work, allowing communication through SSH. 
The next overlay was SLURM, this was chosen as it provided analysis of a complex system with job scheduling and control daemons for specific nodes and allowed roles to become a thing. 
Lastly, K3s was chosen to highlight a commonly used technology and how a cloud application can also be incorporate into the project.

The monitoring was hosted by Glances. 

