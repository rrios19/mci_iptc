import json

def write_macro(cmd,argv):
    macro = {cmd:[{}]}
    for i in argv:
        
    str_macro = json.dumps(macro,indent=2)
    FH = open('data.json','w')
    FH.write(str_macro)
    FH.close()
    print (argv)

params = [1,2,3,4,5]
write_macro('on',argv)




