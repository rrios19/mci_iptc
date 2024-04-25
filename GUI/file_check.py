import paramiko
import time
import json
import os
from pathlib import Path

# Path object for the file
file_path = Path('pathlib_new_file.txt')

# Using 'write_text' for writing text to a file (creates or overwrites)
file_path.write_text("This is some text.")

# Check if the file exists
if not file_path.exists():
    # Using 'touch' to create a file similar to the UNIX touch command
    file_path.touch()





def check_update_status(file_status,file_check):
    # Check if the file_status file exits
    if os.path.exists(file_status):
        # If the file exists, open it and load the dictionary
        with open(file_status, 'r') as file:
            try:
                file_status = json.load(file)
            except json.JSONDecodeError:
                file_status = {}  # Return an empty dictionary if the file is empty or corrupted
            file.close()
    else:
        # If the file does not exist, return an empty dictionary
        file_status = {}

    #Checking if the given path is a directory of a file to handle it accordingly
    dir_split = file_check.split('/')
    if "." in dir_split[len(dir_split)-1]:
        # Path object for the file
        file_path = Path(file_check)
        # Check if the file exists
        if not file_path.exists():
            # Using 'touch' to create a file similar to the UNIX touch command
            file_path.touch()

    else:
        #Check if the actual file or directory exists
        try:
            os.mkdir(file_check)
            print(f"Directory '{file_check}' was created successfully.")
            
        except FileExistsError:
            print(f"Directory '{file_check}' already exists.")

    file_status[file_check:1]




    # Save the dictionary to a file in JSON format
    with open(dir_status, 'w') as updated_file:
        json.dump(file_status, updated_file, indent=4)   
        updated_file.close()


###############################################################################################
# Reading Rpi_dir_status.txt to see if the indicated file/dir exits and create it if it doesn't
###############################################################################################

dir_status = "Rpi_dir_status.txt"
file_check = "file_dir_check.txt"

with open(file_check, "r") as file:
    dir_check = file.readlines()
    file.close()

#Load dictionary containing the file status
check_update_status(dir_status,dir_check)


    


'''
username = 'luis'
hostname = '192.168.43.104'

client = paramiko.SSHClient()
# Add the server's host key automatically without prompting
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

key = paramiko.RSAKey.from_private_key_file('~/.ssh/id_rsa')
client.connect(hostname = hostname, username = username, pkey = key)'''