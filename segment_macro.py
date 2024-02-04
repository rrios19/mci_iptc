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
    # Create an empty list to store the macro sequence
    macro = []
    
    # Get the current time and format it as a string
    time_now = time.localtime()
    time_str = time.strftime("%d-%m-%Y_%H-%M-%S", time_now)
    
    # Read the content of the test_name file and split lines on semicolons
    filehandle = open(test_name)
    lines = re.sub('\s*;\s*', '\n', filehandle.read().strip()).split('\n')
    filehandle.close()
    
    # Process each line of the test_name file
    for line in lines:
        # Split each line into a list using colons as separators and remove leading/trailing spaces
        macro.append(re.sub('[, ]+', ':', line.strip()).split(':'))

    # Generate a new file name for the JSON file based on the current time
    test_json = re.sub('(\.\w+)?$','.json',test_name,count=1)
    test_json = f"{time_str}_{test_json}"

    # Convert the macro list to a JSON-formatted string with indentation
    str_json = json.dumps(macro, indent=2)

    # Write the JSON-formatted macro to a new file in the 'macro' directory
    filehandle = open(f"macro/{test_json}", 'w')
    filehandle.write(str_json)
    filehandle.close()

    # Return the current time and the generated JSON file name
    return time_str, test_json
