import json

usr_dic = {'target':'pi@192.168.1.9','filename':'data.json','logpath':'log/usr_if.log'}
dic_json = {'usr':usr_dic}

str_json = json.dumps(dic_json,indent=2)

filehandle = open('local_conf.json','w')
filehandle.write(str_json)
filehandle.close()

