#import paramiko
import time
import json
import os
from pathlib import Path






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

    # Path object for the file/directory
    file_path = Path(file_check)

    #Checking if the given path is a directory of a file to handle it accordingly
    if file_path.suffix:
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories.:
        
        # Check if the file exists
        if not file_path.exists():
            # Using 'touch' to create a file similar to the UNIX touch command
            file_path.touch()

    else:
        #Check if the actual file or directory 
        try:
            file_path.mkdir(parents=True)         # Create the directory.
            print(f"Directory '{file_check}' was created successfully.")
                
        except FileExistsError:
            print(f"Directory '{file_check}' already exists.")
            
    file_status[file_check] = 1




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
    dir_check = file.readlines()[0].split("\n")[0]
    file.close()

#Load dictionary containing the file status
check_update_status(dir_status,dir_check)


