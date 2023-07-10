# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Basic user interface for MCI
# Usage: $ python3 usr_iface.py

import os
import re
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
    global target
    _,stdout,stderr = client.exec_command(f'cd {workdir} && python3 {topfile}')
    STDOUT = stdout.read().decode().strip().split('\n')
    STDERR = stderr.read().decode().strip()
    print('STDOUT:')
    for line in STDOUT:
        print(line)
    print('STDERR:')
    for line in STDERR:
        print(line)
    target = STDOUT.pop(0) if STDOUT else ''

# Get MCI output file
def get_file():
    files = sftp.listdir(measpath)
    for file in files:
        if re.match(f"{target}.*",file):
            sftp.get(f'{measpath}/{file}',file)

# Fetch usr_iface configurations
conf = fetch_conf('usr')
# Basic configuration for log
configure_log()

# Save arguments
#ARGV = sys.argv
#ARGV.pop(0)

hostname = conf['hostname']
username = conf['username']
password = conf['password']
remote   = conf['remote']
local    = conf['local']
workdir  = conf['workdir']
topfile  = conf['topfile']
measpath = conf['measpath']

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    client.connect(hostname,username=username,password=password)
    sftp = client.open_sftp()

    put_file()
    exec_cmd()
    get_file()

except:
    pass

finally:
    client.close()

