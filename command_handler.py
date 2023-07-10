# Tecnologico de Costa Rica
# Integrated Power Test system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Command handler
# Usage: >>> MACRO = command_handler(test_file)

import sys
import json
import logging

class command_handler:
    def __init__(self):
        self.macro = [] # List of lists, each element is a command
        self.inst = 0   # Same as module identifier
        self.cmd = 0x0  # Current command
        self.ts = 0.3   # Default 0.200 + 0.300 = 0.500
        logging.debug(f'New command_handler object created')

    # Open and load the macro
    def load_macro(self,test_name):
        try:
            filehandle = open(f'macro/{test_name}')
            self.macro = json.load(filehandle)
            filehandle.close()
            logging.info(f'Macro successfully fetched')
            return len(self.macro)
        except:
            logging.error(f'No file test: {test_name}')
            print("No file test") 
            return False

    # Pull out a command from the macro
    def pop_cmd(self):
        return self.macro.pop(0) if self.macro else False

    # Select the current instrument/module identifier
    def set_inst(self,inst):
        self.inst = inst
        logging.debug(f'Instrument changed: {inst}')

    # Return the current instrument identifier
    def get_inst(self):
        return self.inst

    # Set the data in the command
    def set_param(self,value,reset,shift):
        value = int(value) << int(shift) # Parameter value offset
        self.cmd &= int(reset,16) # Current cmd AND reset value
        self.cmd |= value # Current cmd OR parameter value

    # Returns the command to the current instrument and reset the value
    def get_cmd(self):
        cmd = self.cmd # Gets the current command
        self.cmd = 0x0 # Resets the current value
        return cmd

    # Sets the sampling time for measurements
    def set_ts(self,ts):
        self.ts = max(0,float(ts)-0.2) # Limit 0.2

