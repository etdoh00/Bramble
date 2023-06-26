import subprocess
import paramiko
import os
from kubernetes import client, config
import re
#welcoming menu for the user, user enters numbers for the options
def display_menu():
 while True:
  print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  print("                    Hello and welcome to Ethan's Super Computer"                  )
  print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  print("1. Submit a Slurm job")
  print("2. Submit an MPI job")
  print("3. View job queue")
  print("4. View SLURM / MPI job statistics")
  print("5. View database of SLURM/MPI jobs")
  print("6. Benchmark Cluster")
  print("7. Play Minecraft on Kubernetes")
  print("8. Exit Ethan's Super Computer")
  choice = input("Choose your poison: ")

  if choice =="1":
    submit_slurm()
 # elif choice=="2":
 #   submit_kube()
  elif choice =="2":
    submit_mpi()
  elif choice =="3":
    view_stats()
#  elif choice=="5":
 #   view_kube_stats()
  elif choice=="4":
    view_s_output()
  elif choice=="5":
    view_jobs()
  elif choice=="6":
    benchmark()
  elif choice=="7":
    launch_minecraft()
  elif choice=="8":
    print("Goodbye for now, I hope you had fun using Ethan's Super Computer")
    break
  else:
    print("Invalid choice. Please Try again.")
    display_menu()
#uses the SQL database to pull jobs
def view_jobs():
    flag = True
    while flag:
        print()
        print("*********************************************************************")
        print("Welcome to Ethan's Super Computer Database, please choose an option: ")
	#user has 3 choices, view all, view one and leave
        jobsdef = input("Would you like to: \n1. View All Jobs \n2. View a certain job \n3. Leave Database \n-> " )
        #option 1 pulls all info from database
	if jobsdef == "1":
            dball = "sacct"
            os.system(dball)
	#select job to view
        elif jobsdef == "2":
            decision = True
            while decision:
		#build command of job ID
                job_status = input("Enter job ID to view: ")
                command = f"sacct -j {job_status}"
                os.system(command)
		#user can view another job until "n" is entered
                choice = input("Would you like to view another job? Y/N: ")
                if choice.lower() == 'y':
                    continue
                elif choice.lower() == 'n':
                    decision = False
                else:
                    print("Invalid choice. Please choose Y or N.")
	#leave database
        elif jobsdef == "3":
            print("Exited from database")
            print("Goodbye.........")
            print()
            flag = False

def launch_minecraft():
    while True:
	#name pod for deployment
        pod_name = input("What would you like to call the pod? ")
        if pod_name:
	#build command using itzg/minecraft helm charts
            mine_command = f"helm install --version '4.6.1' --namespace minecraft --values minecraft.yaml {pod_name} itzg/minecraft"
            subprocess.run(mine_command, shell=True)
            break
        else:
            print("Please enter a valid pod name.")



def benchmark():
    while True:
	#enter host names for pi's
        hosts = input("Please enter the host names of the pi's to benchmark (comma separated): ")
        if re.match(r'^[a-zA-Z0-9,\s]+$', hosts):
            break
        print("Invalid input. Please enter only alphanumeric characters and commas.")
	#assign number of tasks per node
    while True:
        number = input("Please enter number of tasks per node: ")
        if re.match(r'^\d+$', number):
            break
        print("Invalid input. Please enter only numbers.")
	#submit request
    bench_command = f"mpirun -npernode {number} -host {hosts} hpcc "
    print("Benchmark has begun, please refer to 192.168.0.58 on your browser to see cluster utilisation")
    os.system(bench_command)


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



def submit_mpi():
    while True:
        job_path = input("Enter the path to the MPI Script: ")

        # Check if the file exists
        if not os.path.exists(job_path):
            print("Error: The specified MPI job path does not exist.")
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
        no_nodes= input("Enter the number of nodes: ")
        if no_nodes:
            break
        else:
            print("Error: Please enter a valid number of nodes")

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
                slurm_command = f"sbatch --array=[{size}] --job-name={job_name} --nodes={no_nodes} --time={wall_time} {script_name} "
                break
            else:
                print("Error: Please enter a valid array range.")
    else:
        slurm_command = f"sbatch --job-name={job_name} --nodes={no_nodes} --time={wall_time} {script_name} "
# Submit the MPI job
    os.system(slurm_command)

    # Confirm that the job was submitted
    print("Job submitted successfully.")


def submit_kube():
  job_path = input("Enter the path to the Slurm Script: ")

#check if the file exists
  if not os.path.exists(job_path):
       print("Error: The specified Slurm job path does not exist.")
       return

  config.load_kube_config()

  api_client=client.BatchV1Api()

  with open(job_path) as f:
    job_man = yaml.safe_load(f)

  api_client.create_namespaced_job(
    body=job_man,
    namespace="default"
  )
  print("Kubernetes job submitted successfully")


def view_s_output():
    while True:
	#user enters which job they want to view
        job_id = input("Enter a job ID to view: ")
        if job_id:
	#build command to extract from slurmdbd
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
    print()
	#job output
    print("==============================================JOB OUTPUT===================================================")
    id = f"slurm-{job_id}.out"
    try:
	#custom error message
       result = subprocess.run(['cat',id], capture_output=True, text=True)
       print(result.stdout)
    except FileNotFoundError:
       print(f"Error: File 'slurm-{job_id}.out' is not found or does not have a suitable output format")
    print()
    print()

def view_stats():
    while True:
	#get job from ID
        job_id = input("Enter job ID: ")
        if job_id:
		#build commands
            slurm_command = f"sacct -j {job_id} -o State --noheader"
            result = subprocess.run(slurm_command, shell=True, capture_output=True)
            if result.returncode != 0:
                print("Error retrieving job information: ")
                print(result.stderr.decode())
                exit(1)
            jobstate = result.stdout.decode().strip()
		#output for terminal 
            if jobstate == "COMPLETED":
                print("Job completed successfully.")
            elif jobstate == "FAILED":
                print("Job failed.")
            elif jobstate == "CANCELLED":
                print("Job cancelled.")
            else:
                print("Job is still running or has not started yet")

            command = "squeue --long"
            print("==============================================JOB STATS===================================================")
            print()
            os.system(command)
            print()
            print("==============================================JOB STATS===================================================")
            break
        else:
            print("Please enter a valid job ID.")






# Function to get job statistics by user
def get_user_stats():
    user_stats = {}
    for filename in os.listdir('/var/log/slurm'):
        if re.match(r'slurm-\d{8}$', filename):
            with open(f'/var/log/slurm/{filename}/acct') as f:
                for line in f:
                    if line.startswith('UserId'):
                        user_id = line.split()[1]
                        user_stats[user_id] = user_stats.get(user_id, 0) + 1
    for user, count in user_stats.items():
        print(f'{user}: {count} jobs')

display_menu()
