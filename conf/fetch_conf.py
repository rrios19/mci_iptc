# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Load local configuration.
# Usage: conf = fetch_conf(mod)

import json

def fetch_conf(mod):
    try:
        # Define the path to the local configuration JSON file
        pathfile = 'conf/local_conf.json'
        
        # Open the JSON file for reading
        filehandle = open(pathfile, 'r')
        
        # Load the JSON content into a Python dictionary
        conf = json.load(filehandle)
        
        # Close the file
        filehandle.close()
        
        # Return the specific configuration dictionary based on the provided module key (mod)
        return conf[mod]
    except OSError as err:
        # If an error occurs (e.g., file not found), print the error and return False
        print(err)
        return False
