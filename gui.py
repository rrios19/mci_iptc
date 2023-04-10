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
print(f'Host: {host_name}')
print(f'IP: {host_ip}')

MCI = "pi@192.168.1.9"
DATA = "data.json"

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
        FH = open(DATA,'w')
        FH.write(self.str_json)
        FH.close()
        return self.str_json   

    def send_json(self):
        subprocess.run(['scp',DATA,f"{MCI}:mci_iptc/tmp/{DATA}"])                

ARGV = sys.argv

cmd = ARGV.pop(1)
params = [ARGV[odd] for odd in list(range(1,len(ARGV),2))]
values = [ARGV[even] for even in list(range(2,len(ARGV),2))]

new = macro(cmd,params,values)
#new.show_macro()
new.join_macro()
new.set_json()


