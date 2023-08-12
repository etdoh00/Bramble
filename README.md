# Raspberry Pi HPC Cluster



Welcome to the Raspberry Pi High-Performance Computing (HPC) Cluster repository! This project showcases a powerful HPC cluster built from 10 Raspberry Pi devices, each running headless Debian. The cluster is equipped with K3s, SLURM, and MPI, enabling efficient parallel processing for various computational tasks.

## Features

- **Cluster Configuration:** The Raspberry Pi HPC Cluster consists of 10 Raspberry Pi devices, interconnected to work collaboratively on compute-intensive tasks.
- **K3s Kubernetes:** K3s is employed to manage containerized applications, allowing seamless deployment and scaling across the cluster.
- **SLURM Job Scheduler:** SLURM efficiently manages job scheduling and resource allocation, optimizing workload distribution across the nodes.
- **MPI (Message Passing Interface):** MPI facilitates high-performance communication and coordination between nodes, enabling parallel processing of tasks.
- **Real-Time Monitoring:** Each Raspberry Pi hosts a Glances web server API for real-time system monitoring. This provides insights into resource utilization, temperature, and other vital metrics.
- **Web Interface:** Monitor the cluster's health and performance in real time by accessing the Glances web interface from any web browser.


