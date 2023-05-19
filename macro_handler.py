# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Macro handler
# Usage: >>> macro_name = macro_handler(test_file)

import json

class macro_handler:
    def __init__(self):
        self.freq = 2
        self.macro = [] # List of lists, each element is a command
        self.inst = 0   # Same as module identifier
        self.cmd = 0x0  # Current command
        self.rw   = 0
        #logging.debug(f"New macro object created")

    # Open and load the macro
    def load_macro(self,test_name):
        try:
            filehandle = open(test_name)
            self.macro = json.load(filehandle)
            filehandle.close()
            #logging.info(f"Macro fetched: {self.macro}")
            return len(self.macro)
        except:
            print("No file test") # Revisar esto
            #sys.exit() # Revisar esto

    # Pull out a command from the macro list
    def pop_cmd(self):
        return self.macro.pop(0) if self.macro else False

    # Select the current instrument/module
    def select_inst(self,inst):
        self.inst = inst










    # Return the command to the current instrument
    def get_cmd(self):
        cmd = self.cmd
        self.cmd = 0x0
        return cmd
    

    def get_inst(self):
        return self.inst
    
    # Set the data in the command
    def set_value(self,value,reset,shift):
        value = int(value) << int(shift)
        self.cmd &= int(reset,16) 
        self.cmd |= value

    def set_freq(self,freq):
        self.freq = freq


    def show_cmd(self):
        print(f"CMD: {hex(self.cmd)}")

