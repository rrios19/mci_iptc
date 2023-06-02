# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: User interface for IPTC
# Usage: $ python3 usr_if.py btm velm sas

import os
import sys
import json
import socket
import logging
import subprocess
import paramiko

# For development
#host_name = socket.gethostname()
#host_ip = subprocess.check_output("hostname -I",shell=True,universal_newlines=True).strip()
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

#----------------------------------------------------------------------------------------------

    #except:
    #    pass
    #finally:
    #    client.close()

# Fetch usr_if configurations
#conf = fetch_conf('usr')
# Basic configuration for log
#configure_log()


# Save arguments
#ARGV = sys.argv
#ARGV.pop(0)



hostname = '192.168.1.3'
username = 'rios'
password = '1234'
filename = 'prueba'
remote   = 'prueba.py'
local    = 'prueba.py'
workdir  = 'mci_iptc'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#try:
client.connect(hostname,username=username,password=password)
sftp = client.open_sftp()

sftp.put(local,f'{workdir}/{remote}')

_,stdout,stderr = client.exec_command(f'cd {workdir} && python3 {remote}')
salida_stdout = stdout.read().decode().strip()
salida_stderr = stderr.read().decode().strip()
print('salida stdout:',salida_stdout)
print('salida stderr:',salida_stderr)

sftp.get(f'{workdir}/{remote}',local)
#except:
#    pass
#finally:
#    client.close()


