# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: User interface for IPTC
#           -------   macro    -------
# User -->  | GUI | ---------> | MCI | ...
#           -------   .json    -------

import json
import sys
import subprocess
import socket

host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('----------DEBUG----------')
print(f'Host: {host_name}')
print(f'IP: {host_ip}')
print('-------------------------')

def load_conf():
    confhandle = open('conf/local_conf.json','r')
    conf = json.load(confhandle)
    confhandle.close()
    return conf

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
        return self.macro

    def set_json(self):
        self.str_json = json.dumps(self.macro,indent=2) 
        FH = open(conf['gui']['filename'],'w')
        FH.write(self.str_json)
        FH.close()
        return self.str_json   

    def send_json(self):
        target = conf['gui']['target']
        filename = conf['gui']['filename']
        subprocess.run(['scp',filename,f"{target}:mci_iptc/tmp/{filename}"])

conf = load_conf()

ARGV = sys.argv

cmd = ARGV.pop(1)
params = [ARGV[odd] for odd in list(range(1,len(ARGV),2))]
values = [ARGV[even] for even in list(range(2,len(ARGV),2))]

new = macro(cmd,params,values)
new.join_macro()
new.set_json()
print('Sending')
new.send_json()
print('Running')

