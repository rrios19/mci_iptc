import xml.etree.ElementTree as ET
import os

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
            print(f"\n      Módulo a probar: {Properties.attrib['Selected']}\n      Tipo de prueba: {Properties.attrib['Type']}")


            #On Module_configuration modify the modules attributes for the type of the and the module to be testes.... Set those Here

            #Goes through the sequence to collect the modules needed to excute the test
            print('\n       Módulos necesarios para la prueba\n')
            for module in sequence.iter('Module'):

                #############################################
                #Gets the module's configuration for the test
                #############################################
                
                print(f'       {list(module.attrib.values())[0]}\n       Configuracion de modulo')
                if module[0].attrib:
                    for confKey in list(module[0].attrib):
                        print(f'                {confKey}------->{module[0].attrib[confKey]}')

                else:

                    for step in module[0].iter('Step'):
                        print(f'                 {step.tag}\n                   Pow ------> {step.attrib["Pow"]}\n                  Time --------> {step.attrib["Time"]}')

                ###############################################################################
                #Send a confSettings list to each module used on the test to set its attributes
                ###############################################################################

            seqCnt += 1

        testCnt += 1
GetSequence()