# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: Command management
#  macro   -------   cmd    -------
# -------> | MCI | -------> | MCP | ...
#  .json   -------          -------

import json
import serial

class command_management:
    def __init__(self):
        self.macro  = {} 
        self.cmd    = ''
        self.params = []
	
    def get_macro(self):
        FH = open('data.json')
        self.macro = json.load(FH)
        FH.close()
        return self.macro

    def send_macro(self,argv):
        param = {"a":argv, "b":argv}
        str_json = json.dumps(param,indent=2)
        FH = open('data.json','w')
        FH.write(str_json)
        FH.close
        #return f"Macro: {self.macro}"

    def split_macro(self):
        self.cmd = self.macro['cmd']
        return f"Hello {self.macro}"

    def join_macro(self):
        return f"Hello {self.macro}"

    def sequence_cmd(self):
        return f"Hello {self.macro}"

new = command_management()
test = new.get_macro()
print(test['test'][0]['p'])


#print (command.get_macro())
#str_test = command.get_macro()
#str_test['c'] = 'hola'
#print (str_test)

#print (str_test['a'])
#for i in str_test:
#    print (i)
#command.send_macro('hola')    

