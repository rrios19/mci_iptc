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
from interfaces.spi_master import *

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

def get_scpi():
    filehandle = open("scpi_set.json")
    scpi_set = json.load(filehandle)
    filehandle.close()
    #logging.info(f"Macro fetched: {self.macro}")
    return scpi_set


def get_idn():
    manufacturer = conf["manufacturer"]
    model = conf["model"]
    serial = conf["serial"]
    version = conf["version"]
    print(f"{manufacturer}, {model}, {serial}, {version}.")

def check_iface():
    available = []
    mcps = conf["mcps"]
    ackn = int(conf["acknowledge"],16)
    for mode in mcps:
        spi.change_device(mcps[mode])
        spi.send_data(ackn)
        sleep(0.2)
        if (spi.get_data() == ackn):
            available.append(mode)
    print (available)


class command_handler:
    # Create a new macro object for the current test
    def __init__(self):
        self.macro = [] 
        self.cmd   = []
        self.seq   = []
        #self.params = []
        #self.values = []
        logging.debug(f"New macro object created: '{self.cmd}'")
        	
    # Get the macro, open and load
    def get_macro(self):
        filehandle = open(conf['testname'])
        self.macro = json.load(filehandle)
        filehandle.close()
        logging.info(f"Macro fetched: {self.macro}")
        return self.macro

    def split_macro(self):
        self.cmd = list(self.macro.keys())
        #self.params = list(self.macro[self.cmd].keys())
        #self.values = list(self.macro[self.cmd].values())
       
    def send_macro(self): # Enviar macros al GUI
        #FH = open('output.json','w')
        #FH.write(str_json)
        #FH.close
        print('Enviar macro')


    def join_macro(self):
        return f"Hello {self.macro}"

    def sequence_cmd(self):
        header = hex(conf['header'])
        footer = hex(conf['footer'])
        chain = hex((header<<16) | footer)
        print(f"{chain}")


def cmd_2_bin(RW,MODE,CUR,VOL,POW,RESV):
    RW   <<= 31 #[31]    Read/Write
    MODE <<= 28 #[30-28] Mode
    CUR  <<= 24 #[27-24] Current
    VOL  <<= 16 #[23-16] Voltage
    POW  <<= 8  #[15-08] Power
    #RESV<<= 0  #[07-00] Reserve
    bin_cmd = RW|MODE|CUR|VOL|POW|RESV
    return bin_cmd

# Main
# ------------------------------------------------------
# Fetch usr_if configurations
conf = fetch_conf('mci')
# Basic configuration for log
configure_log()
# Fetch SCPI commands
scpi_set = get_scpi()
# FS, SCLK, CS0, CS1, CS2, MOSI, MISO
spi = iface_handler(400,11,8,7,6,10,9)
# Start SPI clock
spi.start_clk()
# Command input
#while True:
#    scpi_cmd = input("CMD: ")
#    if (scpi_cmd == "exit"):
#        break
#    try:
#        func_to_run = globals()[scpi_set[scpi_cmd]]
#        func_to_run()
#    except:
#        print(f"{scpi_cmd} not available")
macro = command_handler()
macro.get_macro()
sleep(1)
# Kill SPI clock
spi.kill_spi()
# ------------------------------------------------------


#to_test = cmd_2_bin(1,7,0xF,0xFF,0xFF,0xFF)

#try:
#    cmd_prompt = sys.argv
#    func_to_run = globals()[scpi_set[cmd_prompt[1]]]
#    func_to_run()
#except:
#    pass


#Local module
#func_to_run = globals()[dic["*IDN?"]]
#func_to_run()
#Different module
#func_to_run = getattr(other_module,function)
#func_to_run()

#new = command_management()
#macro = new.get_macro()




#print(len(macro))
#new.split_macro()
#new.sequence_cmd()

#print (command.get_macro())
#str_test = command.get_macro()
#str_test['c'] = 'hola'
#print (str_test)

#print (str_test['a'])
#for i in str_test:
#    print (i)
#command.send_macro('hola')    


