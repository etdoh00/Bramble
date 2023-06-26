def benchmark():
    while True:
	#user enters pi host name
        hosts = input("Please enter the host names of the pi's to benchmark (comma separated): ")
	#validate host name
        if re.match(r'^[a-zA-Z0-9,\s]+$', hosts):
            break
        print("Invalid input. Please enter only alphanumeric characters and commas.")
#only enter numbers 
    while True:
        number = input("Please enter number of tasks per node: ")
        if re.match(r'^\d+$', number):
            break
        print("Invalid input. Please enter only numbers.")
#build and submit command
    bench_command = f"mpirun -npernode {number} -host {hosts} hpcc "
    print("Benchmark has begun, please refer to 192.168.0.58 on your browser to see cluster utilisation")
    os.system(bench_command)
