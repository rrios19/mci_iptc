# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Command management
#  macro   -------   cmd    -------
# -------> | MCI | -------> | MCP | ...
#  .json   -------          -------

import os
import re
import sys
import json
import time
import logging
import datetime
import subprocess
from module_handler import *
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

def format_testfile():
    macro = []
    time_now = time.localtime()
    time_str = time.strftime("%d-%m-%Y_%H-%M-%S",time_now)
    filehandle = open(conf['testfile'])
    lines = re.sub(';','\n',filehandle.read().strip()).split('\n')
    for line in lines:
        macro.append(re.sub('\s+',':',line.strip()).split(':'))
    filehandle.close()
    test_json = re.sub('(\.\w+)?$','.json',conf['testfile'],count=1)
    test_json = f"{time_str}_{test_json}"
    str_json = json.dumps(macro,indent=2)
    filehandle = open(test_json,'w')
    filehandle.write(str_json)
    filehandle.close()
    return test_json

# Common commands ----------------------------------------------
def get_idn():
    manufacturer = conf["manufacturer"]
    model = conf["model"]
    serial = conf["serial"]
    version = conf["version"]
    print(f"{manufacturer}, {model}, {serial}, {version}.")

# INSTrument commands ------------------------------------------
class INST:
    def __init__(self,cmd):
        self.parameters = cmd
        self.mcps = {}

    # CATalog, funciona con o sin parametro
    def CAT(self):
        try:
            mcp = self.parameters.pop(0)
            self.mcps[mcp] = conf["ALL"][mcp]
        except:
            self.mcps = conf["ALL"]
        print(self.check_inst())

    def SEL(self):
        device = conf["ALL"][self.parameters.pop(0).upper()]
        macro.conf_inst(device)

    def NSEL(self):
        device = int(self.parameters.pop(0))
        macro.conf_inst(device)

    def INIT(self):
        DEV[conf["BTM"]].start_test()
        DEV[conf["VELM"]].start_test()
        DEV[conf["SAM"]].start_test()

    def check_inst(self):
       available = []
       ack = int(conf["ack"],16)
       for mode in self.mcps:
           spi.change_device(self.mcps[mode])
           spi.send_data(ack)
           sleep(0.20) # Esto debe cambiar
           if (spi.get_data() == ack):
               available.append(mode)
       return available

# CONFigure commands -------------------------------------------
class CONF:
    def __init__(self,cmd):
        self.parameters = cmd

    def TIME(self):
        DEV[macro.get_inst()].conf_time(self.parameters.pop(0))

    def TINT(self):
        cmd = self.parameters.pop(0)
        try:
            DEV[macro.get_inst()].append_wait(cmd)
        except:
            if (cmd.upper() == "STOP"):
                DEV[macro.get_inst()].append_cmd(macro.get_cmd())

    def MODE(self):
        reset = conf["RESET"]["MODE"]
        shift = conf["SHIFT"]["MODE"]
        macro.set_value(self.parameters.pop(0),reset,shift)

    def CURR(self):
        reset = conf["RESET"]["CURR"]
        shift = conf["SHIFT"]["CURR"]
        macro.set_value(self.parameters.pop(0),reset,shift)

    def VOLT(self):
        reset = conf["RESET"]["VOLT"]
        shift = conf["SHIFT"]["VOLT"]
        macro.set_value(self.parameters.pop(0),reset,shift)

    def POW(self):
        reset = conf["RESET"]["POW"]
        shift = conf["SHIFT"]["POW"]
        macro.set_value(self.parameters.pop(0),reset,shift)

    def FREQ(self):
        cmd = self.parameters.pop(0)
        if (cmd.upper() == "OUTP"):
            macro.set_freq(self.parameters.pop(0))
# --------------------------------------------------------------------------------

class macro_handler:
    # Create a new macro object for the current test
    def __init__(self,testfile):
        self.testfile = testfile
        self.freq = 2
        self.macro = []
        self.inst = 0
        self.cmd = 0x0
        self.rw   = 0 # Aun no se que hacer con esto
        logging.debug(f"New macro object created")

    # Fetch the macro, open and read
    def fetch_macro(self):
        try:
            filehandle = open(self.testfile)
            self.macro = json.load(filehandle)
            filehandle.close()
            logging.info(f"Macro fetched: {self.macro}")
            return len(self.macro)
        except:
            print("No file test") # Revisar esto
            sys.exit() # Revisar esto

    # Return the cmd to the current instrument
    def get_cmd(self):
        cmd = self.cmd
        self.cmd = 0x0
        return cmd
    
    def conf_inst(self,inst):
        self.inst = inst

    def get_inst(self):
        return self.inst
    
    # Set the data in the command
    def set_value(self,value,reset,shift):
        try:
            value = int(value) << int(shift)
        except:
            pass # Revisar esto
        self.cmd &= int(reset,16) 
        self.cmd |= value

    def set_freq(self,freq):
        self,freq = freq

    def pop_seq(self):
        for cmd in self.seq:
            print(self.seq)
            device = list(cmd.keys())[0]
            data = int(cmd[device],16)
            spi.change_device(device)
            spi.send_data(data)
            sleep(0.2) # Esto debe cambiar

    def pop_cmd(self):
        cmd = self.macro.pop(0)
        obj_name = cmd.pop(0)
        try:
            atr_name = cmd.pop(0)
            obj_to_call = globals()[scpi_set[obj_name]]
            obj = obj_to_call(cmd)
            atr_to_call = getattr(obj,scpi_set[atr_name])
            atr_to_call()
        except:
            obj_to_call = globals()[scpi_set[obj_name]]
            obj_to_call()

    def show_cmd(self):
        print(f"CMD: {hex(self.cmd)}")

def transfer_spi(device):
    condition = DEV[device].pop_ready()
    data = condition if condition else int(conf["ack"],16) 
    spi.change_device(device)
    spi.send_data(data)
    sleep(0.2) # MODIFICAR ESTO
    response = spi.get_data()
    print(f"{device} : {data} : {response}")

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
# Format the test file into a json file
#testjson = format_testfile()
test_name = format_testfile()
# INST threads
DEV = dict()
DEV[8] = module_handler(8)
DEV[7] = module_handler(7)
DEV[6] = module_handler(6)
# New macro handler
macro = macro_handler(test_name)
macro_len = macro.fetch_macro()
while macro_len > 0:
    macro.pop_cmd()
    macro_len -= 1
    #macro.show_cmd()
    #print("------------------------")

while (DEV[8].check_th()) or (DEV[7].check_th()) or (DEV[6].check_th()):
    if (DEV[8].check_th()): transfer_spi(8)
    if (DEV[7].check_th()): transfer_spi(7) 
    if (DEV[6].check_th()): transfer_spi(6) 
print("FINISH: ALL")



# Kill SPI clock
spi.kill_spi()
# ------------------------------------------------------
#to_test = cmd_2_bin(1,7,0xF,0xFF,0xFF,0xFF)
