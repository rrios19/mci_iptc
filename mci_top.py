# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Command management
#  macro   -------   cmd    -------
# -------> | MCI | -------> | MCP | ...
#  .json   -------          -------

import sys
import json
import logging
#from interfaces.spi_if import *

# Load local configuration
def fetch_conf(mod):
    try:
        path_file = 'conf/local_confi.json'
        confhandle = open(path_file,'r')
        conf = json.load(confhandle)
        confhandle.close()
        return conf[mod]
    except OSError as err:
        print(f"Can not open local configuration file.\n{err}")
        sys.exit()

def configure_log():
    path = conf['logpath']
    if not os.path.exists(path):
        print(f"Creating new log file '{path}'")
    form = '%(levelname)s %(asctime)s %(message)s'
    date = '%H:%M:%S %d/%m/%y'
    verbose = logging.DEBUG
    logging.basicConfig(filename=path,format=form,datefmt=date,level=verbose,filemode='a')



class command_management:
    def __init__(self):
        self.macro  = {} 
        self.cmd    = {}
        self.params = []
        self.values = []
	
    def get_macro(self): # Recibir macros del GUI, watchdog 
        FH = open('data.json')
        self.macro = json.load(FH)
        FH.close()
        return self.macro

    def send_macro(self,argv): # Enviar macros al GUI
        #FH = open('output.json','w')
        #FH.write(str_json)
        #FH.close
        print('Enviar macro')

    def split_macro(self):
        self.cmd = list(self.macro.keys())[0] # One command
        self.params = list(self.macro[self.cmd].keys())
        self.values = list(self.macro[self.cmd].values())

    def join_macro(self):
        return f"Hello {self.macro}"

    def sequence_cmd(self):
        header = 0x0001
        footer = 0x0002
        chain = hex((header<<16) | footer)
        print(f"{chain}")







fetch_conf('mci')

configure_log()

new = command_management()
new.get_macro()
new.split_macro()
new.sequence_cmd()

#print (command.get_macro())
#str_test = command.get_macro()
#str_test['c'] = 'hola'
#print (str_test)

#print (str_test['a'])
#for i in str_test:
#    print (i)
#command.send_macro('hola')    



