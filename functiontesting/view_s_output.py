def view_s_output():
    while True:
        job_id = input("Enter a job ID to view: ")
        if job_id:
            command = ["sacct", "-o", "User,Start,End,Elapsed,JobID,JobName,State,ExitCode", "-j", job_id]
            process = subprocess.Popen(command, stdout=subprocess.PIPE)
            output, error = process.communicate()
            if output:
                print("Job Output: ")
                print(output.decode())
                break
            else:
                print("Error retrieving job output: ", error)
        else:
            print("Please enter a valid job ID.")
