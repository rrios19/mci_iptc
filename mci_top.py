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
    for line in filehandle.readlines():
        macro.append(re.sub('\s+',':',line.strip()).split(':'))
        #macro.append(re.sub('\s+',' ',line.strip()).split(' '))
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

    def CAT(self):
        self.mcps = conf["CAT"]
        self.check_inst()

    def SEL(self):
        device = conf["CAT"][self.parameters.pop(0).upper()]
        macro.conf_inst(device)

    def NSEL(self):
        device = int(self.parameters.pop(0))
        macro.conf_inst(device)

    def check_inst(self):
       available = []
       ack = int(conf["ack"],16)
       for mode in self.mcps:
           spi.change_device(self.mcps[mode])
           spi.send_data(ack)
           sleep(0.2) # Esto debe cambiar
           if (spi.get_data() == ack):
               available.append(mode)
       print(available)

# CONFigure commands -------------------------------------------
class CONF:
    def __init__(self,cmd):
        self.parameters = cmd

    def MODE(self):
        reset = conf["RESET"]["MODE"]
        shift = conf["SHIFT"]["MODE"]
        macro.conf_value(self.parameters.pop(0),reset,shift)

    def CURR(self):
        reset = conf["RESET"]["CURR"]
        shift = conf["SHIFT"]["CURR"]
        macro.conf_value(self.parameters.pop(0),reset,shift)

    def VOLT(self):
        reset = conf["RESET"]["VOLT"]
        shift = conf["SHIFT"]["VOLT"]
        macro.conf_value(self.parameters.pop(0),reset,shift)

    def POW(self):
        reset = conf["RESET"]["POW"]
        shift = conf["SHIFT"]["POW"]
        macro.conf_value(self.parameters.pop(0),reset,shift)

# --------------------------------------------------------------

class command_handler:
    # Create a new macro object for the current test
    def __init__(self,testfile):
        self.testfile = testfile
        self.macro = []
        self.inst = 8
        self.cmd = 0x0
        self.seq = []
        self.rw   = 0
        logging.debug(f"New macro object created")

    # Get the macro, open and read
    def get_macro(self):
        try:
            filehandle = open(self.testfile)
            self.macro = json.load(filehandle)
            filehandle.close()
            logging.info(f"Macro fetched: {self.macro}")
            return len(self.macro)
        except:
            print("No file test") # Revisar esto
            sys.exit() # Revisar esto

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

    def conf_inst(self,inst):
        if (self.cmd != 0x0):
            self.sequence_cmd()
        self.cmd = 0x0
        self.inst = inst

    def conf_value(self,value,reset,shift):
        try:
            value = int(value) << int(shift)
        except:
            pass # Revisar esto
        self.cmd &= int(reset,16) 
        self.cmd |= value

    def sequence_cmd(self):
        aux_dic = {}
        aux_dic[self.inst] = hex(self.cmd)
        self.seq.append(aux_dic)
        print(self.seq)


    def split_macro(self):
        #patron = re.compile("(^\S+)\s(\S+$)")
        #for command in self.macro:
        #    if patron.match(command):
        #        print(command)
        #self.cmd = list(self.macro.keys())
        #self.params = list(self.macro[self.cmd].keys())
        #self.values = list(self.macro[self.cmd].values())
        print("HOLA")
       
    def send_macro(self): # Enviar macros al GUI
        #FH = open('output.json','w')
        #FH.write(str_json)
        #FH.close
        print('Enviar macro')

    def join_macro(self):
        return f"Hello {self.macro}"

    def show_macro(self):
        #print(f"{self.hexcmd:b}")
        #print(hex(self.hexcmd))
        print(f"INST: {self.inst}, CMD: {hex(self.cmd)}")

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
# Format the test file into a json file
#testjson = format_testfile()
test_name = format_testfile()
# New macro handler
macro = command_handler(test_name)
macro_len = macro.get_macro()
while macro_len > 0:
    macro.pop_cmd()
    macro_len -= 1
    macro.show_macro()
    print("------------------------")
macro.sequence_cmd()
sleep(1)
# Kill SPI clock
spi.kill_spi()
# ------------------------------------------------------
#to_test = cmd_2_bin(1,7,0xF,0xFF,0xFF,0xFF)

# Pruebas ----------------------------------------------
#class prueba:
#    def __init__(self):
#        self.word = "hola"
#
#    def greetings(self,name):
#        print(f"{self.word} {name}")
#        #print(f"{self.word}")
#obj = prueba()
#func_2_run = getattr(obj,'greetings')
#func_2_run('ronald')
