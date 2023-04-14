# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: User interface for IPTC
# Usage: $ python3 usr_if.py testname param value ENTER

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

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('----------DEBUG----------')
print(f'Host: {host_name}')
print(f'IP: {host_ip}')
print('-------------------------')

# Load local usr_if configuration. Default path : conf/local_conf.json
def fetch_conf(mod):
    try:
        path_file = 'conf/local_conf.json'
        confhandle = open(path_file,'r')
        conf = json.load(confhandle)
        confhandle.close()
        return conf[mod]
    except OSError as err:
        print(f"Can not open local configuration file.\n{err}\nExiting")
        sys.exit()

def configure_log():
    path = conf['logpath']
    if not os.path.exists(path):
        print(f"Creating new log file '{path}'")
    form = '%(levelname)s %(asctime)s %(message)s'
    date = '%H:%M:%S %d/%m/%y'
    verbose = logging.DEBUG
    logging.basicConfig(filename=path,format=form,datefmt=date,level=verbose,filemode='a')

class macro:
    def __init__(self,cmd,params,values):
        self.cmd      = cmd
        self.params   = params
        self.values   = values
        self.macro    = {}
        self.str_json = ''

    def show_macro(self):
        print(f"{self.cmd}, {self.params}, {self.values}")

    def join_macro(self):
        pair = {par:val for (par,val) in zip(self.params,self.values)} 
        self.macro = {self.cmd:pair}
        logging.debug(f"Macro was joined: {self.macro}")
        return self.macro

    def set_json(self):
        self.str_json = json.dumps(self.macro,indent=2) 
        FH = open(conf['filename'],'w')
        FH.write(self.str_json)
        FH.close()
        logging.debug(f"JSON file was written: '{conf['filename']}'")
        return self.str_json   

    def send_json(self):
        target = conf['target']
        filename = conf['filename']
        subprocess.run(['scp',filename,f"{target}:mci_iptc/tmp/{filename}"])

# Fetch usr_if configurations
conf = fetch_conf('usr')
# Basic configuration for log file
configure_log()

# Save arguments
ARGV = sys.argv
cmd = ARGV.pop(1)
params = [ARGV[odd] for odd in list(range(1,len(ARGV),2))]
values = [ARGV[even] for even in list(range(2,len(ARGV),2))]
# Make macro
new = macro(cmd,params,values)
new.join_macro()
new.set_json()
# Send macro
#new.send_json()



