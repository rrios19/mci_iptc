# Tecnologico de Costa Rica
# Integrated Power Test system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: User interface for IPTC
# Usage: $ python3 usr_if.py btm velm sas

#           ----------   macro    -------
# User -->  | USR_IF | ---------> | MCI | ...
#           ----------   .json    -------

# NOTE: Reception system

import os
import sys
import json
import socket
import logging
import subprocess
import paramiko

# For development
host_name = socket.gethostname()
host_ip = subprocess.check_output("hostname -I",shell=True,universal_newlines=True).strip()
#host_ip = socket.gethostbyname(host_name + ".local")
#host_ip = socket.gethostbyname(host_name + '.')

# Load local usr_if configuration. Default path : conf/local_conf.json
def fetch_conf(mod):
    try:
        path_file = 'conf/local_conf.json'
        confhandle = open(path_file,'r')
        conf = json.load(confhandle)
        confhandle.close()
        return conf[mod]
    except OSError as err:
        print(f"Can not open local configuration file.\n{err}")
        sys.exit()

# Init basic log configurations
def configure_log():
    path = conf['logpath']
    levels = {'DEBUG':10,'INFO':20,'WARNING':30,'ERROR':40,'CRITICAL':50}
    if not os.path.exists(path):
        print(f"Creating new log file '{path}'")
    form = '%(levelname)s %(asctime)s %(message)s'
    date = '%H:%M:%S %d/%m/%y'
    try:
        verbose = levels[conf['verbose']]
    except:
        print(f"Can not set {conf['verbose']} mode. Check local_conf.json file")
        print(f"Available: {list(levels.keys())}")
        sys.exit()
    logging.basicConfig(filename=path,format=form,datefmt=date,level=verbose,filemode='a')
    logging.info(f"Basic log configuration in '{conf['verbose']}' mode")

# Reset test file
def reset_test():
    str_empty = json.dumps({},indent=2)
    filehandle = open(conf['testfile'],'w')
    filehandle.write(str_empty)
    filehandle.close()



class macro:
    # Create a new macro object for the current test
    def __init__(self,cmd,params):
        self.cmd      = cmd
        self.params   = params
        self.values   = []
        self.macro    = {}
        self.str_json = ''
        logging.debug(f"New macro object created: '{self.cmd}'")

    # Print the current macro
    def show_macro(self):
        print(f"{self.cmd}, {self.params}, {self.values}")

    # Set the value to each param
    def set_values(self):
        values = []
        print(f"Setting values for '{self.cmd}'")
        for param in self.params:
            value = input(f"Enter the value for '{param}': ")
            values.append(value)
        self.values = values
        logging.info(f"Values {self.values} were set to '{self.cmd}'")

    # Join the parameters and the values
    def join_macro(self):
        pair = {par:val for (par,val) in zip(self.params,self.values)} 
        self.macro = {self.cmd:pair}
        logging.info(f"Macro was formatted: {self.macro}")
        return self.macro

    # Create a new JSON file with the macro test
    def update_json(self):
        reader = open(conf['testfile'],'r')
        to_append = json.load(reader)
        reader.close()
        update = {**to_append,**self.macro}
        self.str_json = json.dumps(self.macro,indent=2) 
        str_update = json.dumps(update,indent=2) 

        writer = open(conf['testfile'],'w')
        writer.write(str_update)
        writer.close()
        logging.info(f"JSON file was updated: '{conf['testfile']}'")
        return self.str_json   

    # Send JSON to MCI
    def send_json(self):
        ip = conf['ip']
        user = conf['user']
        filename = conf['testfile']
        subprocess.run(['scp',filename,f"{user}@{ip}:mci_iptc/tmp/{filename}"])
        logging.info(f"'{filename}' sent to '{host_ip}'")

    def run_mci():
        host = conf['target']
        user = conf['user']
        password = conf['password']
        rpi = paramiko.SSHClient()
        rpi.load_system_host_keys()
        rpi.connect(host,user,password)

        stdin,stdout,stderr = rpi.exec_command('python3 mici_top.py')
        if stderr.read() == b'':
            for line in stdout.readlines():
                print(line.strip())
        else:
            print(stderr.read())

    # Experimental
    def receive_handler():
        print('hello')


# Fetch usr_if configurations
conf = fetch_conf('usr')
# Basic configuration for log
configure_log()

# Reset test file
reset_test()

# Save arguments
test_seq = []
ARGV = sys.argv
ARGV.pop(0)
for mod in ARGV:
    try:
        test_seq.append(macro(mod,conf[mod]))
    except:
        print(f"Command '{mod}' not found")
        sys.exit()
for cmd in test_seq:
    cmd.set_values()
    cmd.join_macro()
    cmd.update_json()



for i in test_seq:
    i.show_macro()



#cmd = ARGV.pop(1)
#params = [ARGV[odd] for odd in list(range(1,len(ARGV),2))]
#values = [ARGV[even] for even in list(range(2,len(ARGV),2))]
# Make macro
#new = macro(cmd,params,values)
#new.join_macro()
#new.set_json()
# Send macro
#new.send_json()

