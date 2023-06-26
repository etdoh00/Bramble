def submit_slurm():
    while True:
        job_path = input("Enter the path to the Slurm Script: ")

        # Check if the file exists
        if not os.path.exists(job_path):
            print("Error: The specified Slurm job path does not exist.")
        else:
            break

    # Get the job parameters from the user
    while True:
        job_name = input("Enter job name: ")
        if job_name:
            break
        else:
            print("Error: Please enter a valid job name.")

    while True:
        wall_time = input("Enter wall time (in minutes): ")
        if wall_time:
            break
        else:
            print("Error: Please enter a valid wall time.")

    while True:
        script_name = input("Enter the script name: ")
        if script_name:
            break
        else:
            print("Error: Please enter a valid script name.")

    array = input("Is this an array job? Y/N: ")
    if array == "Y":
        while True:
            size= input("Enter the array range:" )
            if size:
                slurm_command = f"sbatch --array=[{size}] --job-name={job_name} --time={wall_time} {script_name} "
                break
            else:
                print("Error: Please enter a valid array range.")
    else:
        slurm_command = f"sbatch --job-name={job_name}  --time={wall_time} {script_name} "

    # Submit the Slurm job
    os.system(slurm_command)

    # Confirm that the job was submitted
    print("Job submitted successfully.")
