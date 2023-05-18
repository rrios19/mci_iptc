# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Macro handler
# Usage: >>> macro_name = macro_handler(test_file)

import json

class macro_handler:
    def __init__(self,testfile):
        self.testfile = testfile # Current test
        self.freq = 2
        self.macro = [] # List of lists, each element is a command
        self.inst = 0   # Same as module identifier
        self.cmd = 0x0  # Current command
        self.rw   = 0
        #logging.debug(f"New macro object created")

    # Fetch the macro, open, and load
    def fetch_macro(self):
        try:
            filehandle = open(self.testfile)
            self.macro = json.load(filehandle)
            filehandle.close()
            #logging.info(f"Macro fetched: {self.macro}")
            return len(self.macro)
        except:
            print("No file test") # Revisar esto
            #sys.exit() # Revisar esto

    # Return the command to the current instrument
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
        value = int(value) << int(shift)
        self.cmd &= int(reset,16) 
        self.cmd |= value

    def set_freq(self,freq):
        self.freq = freq

    def pop_cmd(self):
        return self.macro.pop(0) if self.macro else False

    def show_cmd(self):
        print(f"CMD: {hex(self.cmd)}")

