import os
import json



def build_command(opcode, sender = None, cmdKeyW = None):



    # Open the JSON file for reading
    with open('cmd_codes.json', 'r') as file:
        data = json.load(file)
    
    if sender == "RPI2STM":
         
        if opcode == "sync":
            print(bin(0xff00ff00))

            return 0xff00ff00
        elif opcode == "syncreply":
            return 0x00ff00ff
        
        elif opcode == "reset":
            binOpcode = data[opcode]&((1 << 2) - 1)
            print(data[sender]<<31|binOpcode<<29)
            return data[sender]<<31|binOpcode<<29
        elif opcode == "execute":
            binOpcode = data[opcode]&((1 << 2) - 1)
            print(data[sender]<<31|binOpcode<<29)
            execCmd = data[sender]<<31|binOpcode<<29
            return execCmd
        else:
            binOpcode = data[opcode]&((1 << 2) - 1)
            binOpcode = data[opcode]&((1 << 2) - 1)
            setcmds = []
            for key in list(cmdKeyW.keys()):
                
                if key != 'Selected':
                    KeyBinVal = data[key]&((1 << 4) - 1)

                    literalValues = ['Type','Test','Size']
                    print("KEY: ",key)
                    print("KEYVALUE: ",cmdKeyW[key])
                    if key not in literalValues: 
                        ValbinVal = value_quantization(float(cmdKeyW[key]),key)

                    else:
                        
                        ValbinVal = data[str(cmdKeyW[key])]&((1 << 25) - 1)


                    
                    binCmd = data[sender]<<31|binOpcode<<29|KeyBinVal<<25|ValbinVal


                    print(format(binCmd, '032b'))
                    setcmds.append(binCmd)
            
            return setcmds

        
    




def value_quantization(value,valueType):
    if valueType == 'Current':
        scale = float(1000)  #Scaling the maximum value to 10000 mA

    elif valueType == 'Angle':
        scale = float(36)  #Scaling the maximum value to 360 degrees
    
    elif valueType == 'Rin':
        scale = float(10)  #Scaling the maximum value to 100 Ohms
    
    elif valueType == 'Time':
        scale = float(360) #Scaling the maximum value to 3600 seconds (1 hour)

    else:
        scale = float(1) #Leave default maximum value at 10

    max_value = float(10*scale)

    max_digital_value = (1 << 25) - 1  # 2^25 - 1
    # Resolution
    resolution = max_value / max_digital_value
    digital_value = round(value / resolution)&((1 << 25) - 1)
    return digital_value

