# Tecnologico de Costa Rica
# Integrated Power Test system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Top MCI file
# Usage: $ python3 mci_top.py

import os
import re
import sys
import csv
import json
import datetime
import logging
import datetime
import subprocess
from time import sleep
from conf.fetch_conf import fetch_conf
from segment_macro import segment_macro
from module_handler import module_handler
from command_handler import command_handler
from ifaces.spi_master import iface_handler

# Basic LOG configurations
def configure_log():
    path = conf['logpath']
    # Verbosity levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
    levels = {'DEBUG':10,'INFO':20,'WARNING':30,'ERROR':40,'CRITICAL':50}
    if not os.path.exists(path):
        print(f"Creating new log file '{path}'")
    form = '%(levelname)s %(asctime)s %(message)s'
    date = '%H:%M:%S %d/%m/%y'
    try:
        verbose = levels[conf['verbose']]
    except:
        print(f"Can not set {conf['verbose']} mode. Check local_conf.json")
        print(f"Available: {list(levels.keys())}")
        sys.exit()
    logging.basicConfig(filename=path,format=form,datefmt=date,level=verbose,filemode='a')
    logging.info(f"Basic log configuration in '{conf['verbose']}' mode")

# Load instruction set
def get_scpi():
    filehandle = open("scpi_set.json")
    scpi_set = json.load(filehandle)
    filehandle.close()
    logging.debug(f'SCPI set successfully fetched')
    return scpi_set

# (1) Common commands 
def run_IDN(): # Device identifier
    manufacturer = conf["manufacturer"]
    model = conf["model"]
    serial = conf["serial"]
    version = conf["version"]
    print(f"{manufacturer}, {model}, {serial}, {version}.")
    logging.debug(f'Device identifier command successfully executed')

def run_CLS(): # Clear log
    linux_cmd = ["find", "log/", "-name", "*.log", "-delete"]
    subprocess.run(linux_cmd)
    logging.debug(f'Cleanup command successfully executed')

def run_RST(): # Restore default local_conf and clear log
    linux_cmd = ["cp", "conf/.local_conf.bak", "conf/local_conf.json"]
    subprocess.run(linux_cmd)
    run_CLS()
    logging.debug(f'Reset command successfully executed')

# (2) INSTrument commands
class INST:
    def __init__(self,cmd):
        self.parameters = cmd # Optional parameters
        self.mcps = {}

    # Checks the instrument interface
    def CAT_cmd(self):
        try:
            mcp = self.parameters.pop(0)
            self.mcps[mcp] = conf["ALL"][mcp]
        except:
            self.mcps = conf["ALL"]
        print(self.check_inst())
        logging.info(f'Available instruments: {self.check_inst()}')

    # Selects an instrument as the current instrument
    def SEL_cmd(self):
        device = conf["ALL"][self.parameters.pop(0).upper()]
        MACRO.set_inst(device)
        logging.info(f'Instrument selected: {device}')

    # Selects an instrument as the current instrument
    def NSEL_cmd(self):
        device = int(self.parameters.pop(0))
        MACRO.set_inst(device)
        logging.info(f'Instrument selected: {device}')

    # Initiate the instrument
    def INIT_cmd(self):
        modules = self.parameters if self.parameters else conf["ALL"]
        if "ALL" in modules:
            modules = conf["ALL"]
        for mod in modules:
            MODULE[conf[mod]].start_test()
        logging.info(f'Instrument started: {modules}')

    def check_inst(self):
       available = []
       ack = int(conf["ack"],16)
       for mode in self.mcps:
           SPI.change_device(self.mcps[mode])
           SPI.send_data(ack)
           sleep(0.200) 
           if (SPI.get_data() == ack):
               available.append(mode)
       return available

# (3) CONFigure commands
class CONF:
    def __init__(self,cmd):
        self.parameters = cmd # Optional parameters

    # Sets the test time
    def TIME_cmd(self):
        MODULE[MACRO.get_inst()].conf_time(self.parameters.pop(0))
        logging.info(f'Time setting successful')
    
    # Sets the time interval
    def TINT_cmd(self):
        cmd = self.parameters.pop(0)
        if cmd.isdigit():
            MODULE[MACRO.get_inst()].append_time(cmd)
            logging.info(f'Time interval started')
        elif cmd.upper() == "END":
            MODULE[MACRO.get_inst()].append_cmd(MACRO.get_cmd())
            logging.info(f'Time interval finished')

    # Sets the mode for the instrument
    def MODE_cmd(self):
        reset = conf["RESET"]["MODE"]
        shift = conf["SHIFT"]["MODE"]
        MACRO.set_param(self.parameters.pop(0),reset,shift)
        logging.debug(f'Mode set successfully')

    # Sets the current value
    def CURR_cmd(self):
        reset = conf["RESET"]["CURR"]
        shift = conf["SHIFT"]["CURR"]
        MACRO.set_param(self.parameters.pop(0),reset,shift)
        logging.debug(f'Current set successfully')

    # Sets the voltage value
    def VOLT_cmd(self):
        reset = conf["RESET"]["VOLT"]
        shift = conf["SHIFT"]["VOLT"]
        MACRO.set_param(self.parameters.pop(0),reset,shift)
        logging.debug(f'Voltage set successfully')

    # Sets the power value
    def POW_cmd(self):
        reset = conf["RESET"]["POW"]
        shift = conf["SHIFT"]["POW"]
        MACRO.set_param(self.parameters.pop(0),reset,shift)
        logging.debug(f'Power set successfully')

    # Sets the sampling time
    def SAMP_cmd(self):
        MACRO.set_ts(self.parameters.pop(0))
        logging.debug(f'Sampling time set successfully')

# (4) MEASure commands
class MEAS:
    def __init__(self,cmd):
        self.parameters = cmd # Optional parameters

    # Reads the voltage of the instrument using an optional scale
    def VOLT_cmd(self):
        scale = self.parameters.pop(0) if self.parameters else 1
        MEASURE[MACRO.get_inst()].set_scale("VOLT",scale)   # Set scale
        MEASURE[MACRO.get_inst()].set_measure("VOLT")       # Set identifier
        logging.info(f'Voltage measurement with scale equal to {scale}')

    # Reads the current of the instrument using an optional scale
    def CURR_cmd(self):
        scale = self.parameters.pop(0) if self.parameters else 1
        MEASURE[MACRO.get_inst()].set_scale("CURR",scale)   # Set scale
        MEASURE[MACRO.get_inst()].set_measure("CURR")       # Set identifier
        logging.info(f'Current measurement with scale equal to {scale}')

    # Reads the power of the instrument using an optional scale
    def POW_cmd(self):
        scale  = self.parameters.pop(0) if self.parameters else 1
        MEASURE[MACRO.get_inst()].set_scale("POW",scale)    # Set scale
        MEASURE[MACRO.get_inst()].set_measure("POW")        # Set identifier
        logging.info(f'Power measurement with scale equal to {scale}')

    def RES_cmd(self):
        scale  = self.parameters.pop(0) if self.parameters else 1
        # Equation here
        logging.info(f'Resistance measurement with scale equal to {scale}')

# (5) SYSTem commands
class SYST:
    def __init__(self,cmd):
        self.parameters = cmd # Optional parameters

    # Prints the last error message
    def ERR_cmd(self):
        path = conf['logpath'] # LOG file
        filehandle = open(path,'r')
        queue = filehandle.readlines()
        filehandle.close()
        for msg in queue:
            if re.search('ERROR', msg): # Looking for ERROR
                queue.remove(msg) # Remove ERROR from the queue
                print(msg.strip()) # Print ERROR
        filehandle = open(path,'w') # Overwrite LOG file
        filehandle.writelines(queue) # Write the new queue
        filehandle.close()

# (6) MEMory commands
class MEM:
    def __init__(self,cmd):
        self.parameters = cmd # Optional parameters

    # Prints the name of the current files saved in memory
    def CAT_cmd(self):
        # Default: ALL?
        select = self.parameters.pop(0) if self.parameters else 'ALL?' 
        directories = conf['filetype'][select]
        for folder in directories:
            files = os.listdir(folder)
            for item in files:
                print(f'{item}, {folder}') # filename, typename

    # Delete the specified file from memory
    def DEL_cmd(self):
        target = self.parameters.pop(-1) if self.parameters else '*'
        print(target)
        folder = self.parameters.pop(0) if self.parameters else 'ALL'
        print(folder)
        folder = conf['filetype'][folder]
        for fd in folder:
            linux_cmd = ["find", f"{fd}/", "-name", target, "-delete"]
            subprocess.run(linux_cmd)

# Measurement handler
class measure_handler:
    def __init__(self,inst,test_time):
        self.inst = inst
        self.test_time = test_time
        self.init_time = 0
        self.measurements = []
        self.scale = {}

    def set_measure(self,measure):
        self.measurements.append(measure)
        logging.info(f'Measurement: {measure}')

    def set_scale(self,param,scale):
        self.scale[param] = scale

    def get_param(self,measure):
        if not self.init_time and self.measurements:
            write_csv(self.test_time,self.inst,['time',*self.measurements])
            self.init_time = datetime.datetime.now()
        params = []
        for param in self.measurements:
            value = measure & ~int(conf["RESET"][param],16) 
            value = value >> conf["SHIFT"][param]
            params.append(value * float(self.scale[param]))
        if self.measurements:
            time_now = datetime.datetime.now()
            dt = (time_now - self.init_time).total_seconds()
            write_csv(self.test_time,self.inst,[round(dt,3),*params])

# Command interpreter
def run_cmd(cmd):
    class_name = cmd.pop(0)
    func_to_call = globals()[scpi_set[class_name]]
    if cmd:
        atr_name = cmd.pop(0)
        obj = func_to_call(cmd)
        func_to_call = getattr(obj,scpi_set[atr_name])
    func_to_call()

# Transfer data by SPI
def transfer_spi(device):
    condition = MODULE[conf[device]].pop_ready()
    data = condition if condition else int(conf["ack"],16) 
    SPI.change_device(conf[device])
    SPI.send_data(data)
    sleep(0.2) # MODIFICAR ESTO
    response = SPI.get_data()
    if (response !=  int(conf["ack"],16)):
        MEASURE[conf[device]].get_param(response)
    print(f"{conf[device]} : {data} : {response}")
    sleep(MACRO.ts)

# Write to a CSV file
def write_csv(test_time,module,row):
    path = f"measurement/{test_time}_{module}.csv"
    with open(path,'a') as filehandle:
        writer = csv.writer(filehandle)
        writer.writerow(row)
        filehandle.close()

# Fetch configurations
conf = fetch_conf('mci')
# Basic configuration for LOG
configure_log()
# Fetch SCPI commands
scpi_set = get_scpi()
# FS, SCLK, CS0, CS1, CS2, MOSI, MISO
SPI = iface_handler(200,11,8,7,6,10,9) # Fs = 200 Hz
# Start SPI clock
SPI.start_clk()
# Format the test file into a json file
test_time,test_name = segment_macro(conf['testfile'])
print(f'{test_name}')

# INST/MODULE threads
MODULE = dict()
MODULE[conf['BTM']]  = module_handler()
MODULE[conf['VELM']] = module_handler()
MODULE[conf['SAM']]  = module_handler()

# Measurement handler
MEASURE = dict()
MEASURE[conf["BTM"]]  = measure_handler("BTM",test_time)
MEASURE[conf["VELM"]] = measure_handler("VELM",test_time)
MEASURE[conf["SAM"]]  = measure_handler("SAM",test_time)

# MACRO handler
MACRO = command_handler()
msize = MACRO.load_macro(test_name)

while msize > 0:
    run_cmd(MACRO.pop_cmd())
    msize -= 1

while MODULE[8].check_thread() or MODULE[7].check_thread() or MODULE[6].check_thread():
    if (MODULE[8].check_thread()): transfer_spi('BTM')
    if (MDOULE[7].check_thread()): transfer_spi('VELM') 
    if (MODULE[6].check_thread()): transfer_spi('SAM') 

# Kill SPI clock
SPI.kill_spi()

