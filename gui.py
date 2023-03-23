# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: User interface for IPTC
#           -------   macro    -------
# User -->  | GUI | ---------> | MCI | ...
#           -------   .json    -------

import json

class macro:
    def __init__(self,cmd,params,values):
        self.cmd      = cmd
        self.params   = params
        self.values   = values
        self.macro    = {}
        self.str_json = ''

    def show_macro(self):
        print(f"{self.cmd}, {self.params}, {self.values}")

    def join_macro(self):
        pair = {par:val for (par,val) in zip(self.params,self.values)} 
        self.macro = {self.cmd:[pair]}
        print(self.macro)

    def get_json(self):
        self.str_json = json.dumps(self.macro,indent=2) 
        FH = open('data.json','w')
        FH.write(self.str_json)
        FH.close()
        print(self.str_json)    
    
params = ['ten','cor','cic']
values = [12,1,5]

new = macro('on',params,values)
new.show_macro()
new.join_macro()
new.get_json()

#print(macro_test["on"][0]['ten'])

