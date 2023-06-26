def view_jobs():
    while True:
        job_status = input("Enter job status to view (e.g. 'RUNNING', 'COMPLETED'): ")
        command = f"sacct -S -n -P -o jobid,jobname,state,exitcode,submit,start,end -t {job_status}"
        output = os.popen(command).read()

        if output:
            print(output)
            break
        else:
            print("Invalid job status. Please try again.")

def launch_minecraft():
    while True:
        pod_name = input("What would you like to call the pod? ")
        if pod_name:
            mine_command = f"helm install --version '4.6.1' --namespace minecraft --values minecraft.yaml {pod_name} itzg/mi"
            subprocess.run(mine_command, shell=True)
            break
        else:
            print("Please enter a valid pod name.")

