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
import csv
import json
import time
import logging
import datetime
import subprocess
from segment_macro import *
from module_handler import *
from macro_handler import *
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
        macro.set_inst(device)

    def NSEL(self):
        device = int(self.parameters.pop(0))
        macro.set_inst(device)

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
            DEV[macro.get_inst()].append_time(cmd)
        except:
            if (cmd.upper() == "STOP"):
                DEV[macro.get_inst()].append_cmd(macro.get_cmd())

    def MODE(self):
        reset = conf["RESET"]["MODE"]
        shift = conf["SHIFT"]["MODE"]
        macro.set_param(self.parameters.pop(0),reset,shift)

    def CURR(self):
        reset = conf["RESET"]["CURR"]
        shift = conf["SHIFT"]["CURR"]
        macro.set_param(self.parameters.pop(0),reset,shift)

    def VOLT(self):
        reset = conf["RESET"]["VOLT"]
        shift = conf["SHIFT"]["VOLT"]
        macro.set_param(self.parameters.pop(0),reset,shift)

    def POW(self):
        reset = conf["RESET"]["POW"]
        shift = conf["SHIFT"]["POW"]
        macro.set_param(self.parameters.pop(0),reset,shift)

    def FREQ(self):
        cmd = self.parameters.pop(0)
        if (cmd.upper() == "OUTP"):
            macro.set_freq(self.parameters.pop(0))
# --------------------------------------------------------------------------------

def run_cmd(cmd):
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


def transfer_spi(device):
    condition = DEV[conf[device]].pop_ready()
    data = condition if condition else int(conf["ack"],16) 
    spi.change_device(conf[device])
    spi.send_data(data)
    sleep(0.2) # MODIFICAR ESTO
    response = spi.get_data()
    print(f"{conf[device]} : {data} : {response}")
    write_csv(device,[conf[device],response])

def write_csv(module,row):
    with open(f"{module}.csv",'a') as filehandle:

        writer = csv.writer(filehandle)
        writer.writerow(row)

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
test_name = segment_macro(conf['testfile'])
# INST threads
DEV = dict()
DEV[8] = module_handler(8)
DEV[7] = module_handler(7)
DEV[6] = module_handler(6)
# New macro handler
macro = macro_handler()
macro_len = macro.load_macro(test_name)
while macro_len > 0:
    run_cmd(macro.pop_cmd())
    macro_len -= 1
    #macro.show_cmd()
    #print("------------------------")

while (DEV[8].check_thread()) or (DEV[7].check_thread()) or (DEV[6].check_thread()):
    if (DEV[8].check_thread()): transfer_spi('BTM')
    if (DEV[7].check_thread()): transfer_spi('VELM') 
    if (DEV[6].check_thread()): transfer_spi('SAM') 
print("FINISH: ALL")



# Kill SPI clock
spi.kill_spi()
# ------------------------------------------------------
#to_test = cmd_2_bin(1,7,0xF,0xFF,0xFF,0xFF)
