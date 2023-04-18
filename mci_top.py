# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Command management
#  macro   -------   cmd    -------
# -------> | MCI | -------> | MCP | ...
#  .json   -------          -------

import os
import sys
import json
import logging
#from interfaces.spi_if import *

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
    logging.info(f"Running {sys.argv[0]}")
    logging.info(f"Basic log configuration in '{conf['verbose']}' mode")

class command_management:
    # Create a new macro object for the current test
    def __init__(self):
        self.macro  = {} 
        self.cmd    = {}
        self.params = []
        self.values = []
        logging.debug(f"New macro object created: '{self.cmd}'")
        	
    # Get the macro, open and load
    def get_macro(self):
        FH = open('data.json')
        self.macro = json.load(FH)
        FH.close()
        logging.info(f"Macro fetched: {self.macro}")
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
        header = hex(conf['header'])
        footer = hex(conf['footer'])
        chain = hex((header<<16) | footer)
        print(f"{chain}")


# Fetch usr_if configurations
conf = fetch_conf('mci')
# Basic configuration for log
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



