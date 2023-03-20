# MCI IPTC
# Author: Ronald Rios
# Description: Link by ssh and run the app

import json

class command_management:
    
    def __init__(self,macro):
        self.macro = macro

    def get_macro(self):
        FH = open('data.json')
        self.macro = json.load(FH)
        FH.close()
        return f"Macro: {self.macro}"

    def send_macro(self):
        return f"Macro: {self.macro}"

    def split_macro(self):
        return f"Hello {self.macro}"

    def join_macro(self):
        return f"Hello {self.macro}"

    def sequence_cmd(self):
        return f"Hello {self.macro}"

command = command_management("12345678")

print (command.get_macro())
    
