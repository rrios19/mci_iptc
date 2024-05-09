import xml.etree.ElementTree as ET
import os
from command_handler import build_command as buildcmd
import json
###Desde la PC se debe mandar la instrucción de escribir en file_dir_check.txt
###la dirección donde están los tests que se quieren ejecutar.

def CheckQueuedTestsPath():
    #Opens the file that contains the path to the queued tests
    with open("file_dir_check.txt","r") as queuedTestsPath:
        Tests = queuedTestsPath.readlines()[0].split('\n')[0]
        queuedTestsPath.close()
    return Tests


def GetSequence():
    #Get all the queued tests
    TestsPath = CheckQueuedTestsPath()
    with open(TestsPath, "r") as queuedPath:
        TestsNames = queuedPath.readlines()
        queuedPath.close()

    testCnt = 1
    
    for Test in TestsNames: 
        print(f"\n\nPrueba {testCnt}: {Test}")
        # Parse the XML file    
        TestPath = TestsPath.replace("queued_tests.txt",Test.split('\n')[0])
        tree = ET.parse(TestPath)   
        root = tree.getroot()   

        seqCnt = 1

        
        for sequence in root.iter('Sequence'):

            #################################################################################
            #Extracts the sequence properties (The module to be tested and the type of test)
            #################################################################################
                   
    
            print(f'\n \n   Secuencia {seqCnt}\n')
            Properties = sequence.find('Sequence_Properties')[0]
            testedModName = Properties.attrib['Selected']
            testType = Properties.attrib['Type']
            print(f"\n      Módulo a probar: {testedModName}\n      Tipo de prueba: {testType}")


            #On Module_configuration modify the modules attributes for the type of the and the module to be testes.... Set those Here

            #Goes through the sequence to collect the modules needed to excute the test
            print('\n       Módulos necesarios para la prueba\n')

                

            cmds = {}
            synCmd = buildcmd("sync","RPI2STM")
            cmds['sync'] = synCmd
            
            for module in sequence.iter('Module'):
                cmd_x = {} #This list will have every keyword needed for each parameter setting instruction
                #############################################
                #Gets the modules' configuration for the test
                #############################################

                print(f'                       Configuracion de modulo')



                for confKey in list(module.attrib):
                    print(f'                {confKey}------->{module.attrib[confKey]}')

                    ###To get started with the instruction build 
                    cmd_x[confKey] = module.attrib[confKey]


                for step in module.iter('Step'):
                    print(f'                {step.tag}')
                    stepAttr = step.attrib
                
                    cmd_x[stepAttr['Step_type']] = stepAttr['type_value']
                    cmd_x['Time'] = stepAttr['Time']
                    #cmd_x.append(step.attrib[1])
                    #for stepAttrib in list(step.attrib.keys()):
                    #    print(f'                    {stepAttrib} ------> {step.attrib[stepAttrib]}')
                    #    cmd_x.append({stepAttrib: step.attrib[stepAttrib]})
                ################################################################################
                # Send a confSettings list to each module used on the test to set its attributes
                ################################################################################
                if cmd_x['Selected'] == testedModName:   #Since the module to be tested is declared twice in every sequence, specifying 
                                               #first the it is going to be tested and the the setting it will need
                                               #we need a way to not add it twice to the cmd list but to know if is the tested one.
                    cmd_x['Type'] = testType
                    try:
                        cmd_x['Test'] = Properties.attrib["Test"]
                    except:
                        pass
                else:
                    cmd_x['Type'] = None
                
                seqCmds = buildcmd("set","RPI2STM",cmd_x)
                
                cmds[cmd_x['Selected']] = seqCmds
                print(f'Comando individual: {cmd_x}')

            
            execCmd = buildcmd("execute","RPI2STM")

            replyCmd = buildcmd("syncreply", "RPI2STM")
            
            cmds['execute'] = execCmd

            cmds['syncreplay'] = replyCmd

            # Convert to JSON
            json_cmds = json.dumps(cmds, indent=4)
            
            instPath = TestsPath.replace('queued_tests.txt','seqInstruction.json')

            with open(instPath, 'w') as instructionFile:
                instructionFile.write(json_cmds)


                
            #cmds.append("RPI2STM","set",cmd_x)
            #print(f'Comandos de la secuencia: {cmds}')
            seqCnt += 1

        testCnt += 1
GetSequence()