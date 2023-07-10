# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Basic user interface for MCI
# Usage: $ python3 usr_iface.py

import os
import sys
import json
import socket
import logging
import paramiko
import subprocess
from conf.fetch_conf import fetch_conf

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

# Put the macro file inside MCI
def put_file():
    sftp.put(local,f'{workdir}/{remote}')

# Execute the MCI and wait for the STDOUT and STDERR
def exec_cmd():
    _,stdout,stderr = client.exec_command(f'cd {workdir} && python3 {remote}')
    salida_stdout = stdout.read().decode().strip()
    salida_stderr = stderr.read().decode().strip()
    print('salida stdout:',salida_stdout)
    print('salida stderr:',salida_stderr)

# Get MCI output file
def get_file():
    sftp.get(f'{workdir}/{remote}',local)

# Fetch usr_iface configurations
#conf = fetch_conf('usr')
# Basic configuration for log
#configure_log()

# Save arguments
#ARGV = sys.argv
#ARGV.pop(0)

hostname = '172.20.1.4'
username = 'rios'
password = '1234'
filename = 'prueba'
remote   = 'testfile'
local    = 'testfile'
workdir  = 'mci_iptc'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#try:
client.connect(hostname,username=username,password=password)
sftp = client.open_sftp()

put_file()
exec_cmd()
get_file()

#except:
#    pass
#finally:
#    client.close()


# For development
#host_name = socket.gethostname()
#host_ip = subprocess.check_output("hostname -I",shell=True,universal_newlines=True).strip()
#host_ip = socket.gethostbyname(host_name + ".local")
#host_ip = socket.gethostbyname(host_name + '.')
