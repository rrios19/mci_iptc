# Tecnologico de Costa Rica
# Integrated Power Testing system for CubeSats (IPTC)
# Control and interface module
# Author: Ronald Rios
# Description: MCI configuration tool
# Usage: $ python3 mci-config.py

import os
import sys
import json

# Extract command-line arguments and pop the script name
ARGV = sys.argv
ARGV.pop(0)

# If arguments are provided, use the first one as the filename; otherwise, use 'local_conf.json'
filename = ARGV.pop(0) if ARGV else 'local_conf.json'
print(filename)

# Open the specified configuration file and load its contents into local_conf dictionary
filehandle = open(filename, 'r')
local_conf = json.load(filehandle)
filehandle.close()

# Handle the menu using hashes
def menu_handler(dic):
    keys = list(dic.keys())
    for k in keys:
        num = keys.index(k)
        print(f"{num + 1}: {k}")
    print(f"{num + 2}: Save and exit")
    print('Enter another [KEY] to exit without saving')
    try:
        option = int(input('Select an option: '))
        if option == num + 2:
            save_conf()
            sys.exit()
        elif option < 1:
            sys.exit()
        selected = keys[option - 1]
        return selected
    except:
        sys.exit()

# Change the value of the hash
def change_conf(key, val):
    print(f"Currently: {key} = {val}")
    new = input(f"Enter the new value for '{key}': ")
    local_conf[mod_key][chg_key] = new
    print(f"\nTask completed successfully. Now '{key}' is equal to '{new}'\n")

# Save, write changes in local_conf.json
def save_conf():
    try:
        filehandle = open(filename, 'w')
        str_json = json.dumps(local_conf, indent=2)
        filehandle.write(str_json)
        filehandle.close()
        print(f"Save and exit. Task completed successfully.")
    except:
        print('Can not save changes')

# Main loop, for select and change
while True:
    print('MCI Software Configuration Tool (mci-config)')
    mod_key = menu_handler(local_conf)
    print("\nMCI Software Configuration Tool (mci-config)")
    chg_key = menu_handler(local_conf[mod_key])
    print("\nMCI Software Configuration Tool (mci-config)")
    change_conf(chg_key, local_conf[mod_key][chg_key])
