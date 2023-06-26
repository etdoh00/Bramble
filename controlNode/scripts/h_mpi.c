#include <stdio.h>
#include <mpi.h>

int main(int argc, char** argv) {
 int node;
 MPI_Init (&argc, &argv);
 MPI_Comm_rank(MPI_COMM_WORLD, &node);

 printf("Hello from node %d!\n", node);
 MPI_Finalize();
}


