# Tecnologico de Costa Rica
# Integrated Power Test system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Sequence the macro into a list
# Usage: >>> new_test_name = segment_macro(test_name)

import re
import json
import time

def segment_macro(test_name):
    macro = []
    time_now = time.localtime()
    time_str = time.strftime("%d-%m-%Y_%H-%M-%S",time_now)
    filehandle = open(test_name)
    lines = re.sub('\s*;\s*','\n',filehandle.read().strip()).split('\n')
    filehandle.close()
    for line in lines:
        macro.append(re.sub('[, ]+',':',line.strip()).split(':'))
    test_json = re.sub('(\.\w+)?$','.json',test_name,count=1)
    test_json = f"{time_str}_{test_json}"
    str_json = json.dumps(macro,indent=2)
    filehandle = open(f"macro/{test_json}",'w')
    filehandle.write(str_json)
    filehandle.close()
    return time_str,test_json

