def launch_minecraft():
#define pod name
    while True:
        pod_name = input("What would you like to call the pod? ")
        if pod_name:
#build command and submit
            mine_command = f"helm install --version '4.6.1' --namespace minecraft --values minecraft.yaml {pod_name} itzg/mineecraft"
            subprocess.run(mine_command, shell=True)
            break
        else:
            print("Please enter a valid pod name.")
