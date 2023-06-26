import subprocess
import paramiko
import os
from kubernetes import client, config

def display_menu():
 while True:
  print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  print("                    Hello and welcome to Ethan's Super Computer"                  )
  print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  print("1. Submit a Slurm job")
  print("2. Submit an MPI job")
  print("3. View Slurm Queue")
  print("4. View SLURM / MPI Stats")
  print("5. View all SLURM/MPI jobs")
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

def view_jobs():
  command=f"sacct"
  os.system(command)


def launch_minecraft():
    pod_name = input("What would you like to call the pod?")
    mine_command =f"helm install --version '4.6.1' --namespace minecraft --values minecraft.yaml {pod_name} itzg/minecraft"
    os.system(mine_command)

def benchmark():
   hosts = input("Please enter the host names of the pi's to benchmark (comma seperated): ")
   number = input("Please enter number of tasks per node: ")
   bench_command = f"mpirun -npernode {number} -host {hosts} hpcc "
   print("Benchmark has begun, please refer to 192.168.0.58 on your browser to see cluster utilisation") 
   os.system(bench_command)
   

def submit_slurm():
  #user needs to use a file path to insert the script
   job_path = input("Enter the path to the Slurm Script: ")

#check if the file exists
   if not os.path.exists(job_path):
       print("Error: The specified Slurm job path does not exist.")
       return

    # Get the job parameters from the user
   job_name = input("Enter job name: ")
#   num_nodes = input("Enter number of nodes: ")
#   num_tasks = input("Enter number of tasks: ")
   wall_time = input("Enter wall time (in minutes): ")
   script_name= input("Enter the script name: ")
   array = input("Is this an array job? Y/N: " )
   if array == "Y":
       size= input("Enter the array range:" )
       slurm_command = f"sbatch --array=[{size}] --job-name={job_name} --time={wall_time} {script_name} "
   else:
    # Construct the Slurm command
       slurm_command = f"sbatch --job-name={job_name}  --time={wall_time} {script_name} "
    # Submit the Slurm job
   os.system(slurm_command)

    # Confirm that the job was submitted
   print("Job submitted successfully.")

def submit_mpi():
   #similar to slurm. user will be asked to for their path to the mpi script
   mpi_path=input("Enter the path to the MPI Script: ")

   if not os.path.exists(mpi_path):
      print("Error: The MPI script does not exist")
      return

   job_name = input("Enter job name: ")
   num_nodes = input("Enter number of nodes: ")
   num_tasks = input("Enter number of tasks: ")
   wall_time = input("Enter wall time (in minutes): ")
   script_name= input("Enter the script name: ")

   slurm_command = f"sbatch --job-name={job_name} --nodes={num_nodes} --ntasks={num_tasks} --time={wall_time} {script_name} "
   os.system(slurm_command)

   print("Job Submitted Successfully.")


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
  print("Enter a job ID to view:" )
  job_id=input()

  command=["sacct","-o","User,Start,End,Elapsed,JobID,JobName,State,ExitCode","-j",job_id]
  process=subprocess.Popen(command, stdout=subprocess.PIPE)
  output, error = process.communicate()

  if output:
   print("Job Output: ")
   print(output.decode())
  else:
   print("Error retrieving job output: ", error)

def view_stats():
  job_id = input("Enter job ID: ")
  slurm_command = f"sacct -j {job_id} -o State --noheader"
  result = subprocess.run(slurm_command, shell=True, capture_output=True)
  if result.returncode != 0:
      print("Error retrieving job information: ")
      print(result.stderr.decode())
      exit(1)
  jobstate = result.stdout.decode().strip()


  if jobstate == "COMPLETED":
      print("Job completed successfully.")
  elif jobstate == "FAILED":
     print("Job failed. ")
  elif jobstate == "CANCELLLED":
     print("Job cancelled.")
  else:
     print("Job is still running or has not started yet")

  command = f"squeue --long"
  print("==============================================JOB STATS===================================================")
  print()
  os.system(command)
  print()
  print("==============================================JOB STATS===================================================")


import os
import re

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
