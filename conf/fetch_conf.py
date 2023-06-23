# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and Interface Module
# Author: Ronald Rios
# Description: Load local configuration.
# Usage: conf = fetch_conf(mod)

import json

def fetch_conf(mod):
    try:
        pathfile = 'conf/local_conf.json'
        filehandle = open(pathfile,'r')
        conf = json.load(filehandle)
        filehandle.close()
        return conf[mod]
    except OSError as err:
        print(err)
        return False

