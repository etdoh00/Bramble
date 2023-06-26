def view_stats():
    while True: #get job ID
        job_id = input("Enter job ID: ")
	#build slurm command
        if job_id:
            slurm_command = f"sacct -j {job_id} -o State --noheader"
            result = subprocess.run(slurm_command, shell=True, capture_output=True)
	    #check if complete
            if result.returncode != 0:
                print("Error retrieving job information: ")
                print(result.stderr.decode())
                exit(1)
            jobstate = result.stdout.decode().strip()
		#review job states
            if jobstate == "COMPLETED":
                print("Job completed successfully.")
            elif jobstate == "FAILED":
                print("Job failed.")
            elif jobstate == "CANCELLED":
                print("Job cancelled.")
            else:
                print("Job is still running or has not started yet")
		#show running jobs
            command = "squeue --long"
            print("==============================================JOB STATS===================================================")
            print()
            os.system(command)
            print()
            print("==============================================JOB STATS===================================================")
            break
        else:
            print("Please enter a valid job ID.")
