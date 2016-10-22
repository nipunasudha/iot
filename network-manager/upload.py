import os
import time
import json
data={}
#============= SETTINGS READER ==================
def update():
    try:
        jsonFile = open("../Settings.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()
    except:
        print('Settings Write Error!')
def read():
    global data
    returndata=data
    try:
        jsonFile = open("../Settings.json", "r")
        returndata = json.load(jsonFile)
        jsonFile.close()
    except:
        print('Settings Read Error!')
    return returndata


#============= UPLOADER ==================

print("===========================================")
print("DATA UPLOADER LAUNCHER SERVICE\n")
while 1:
    #------------------------------------------------------------
    data=read()
    interval=float(data['settings']['interval'])
    interval=1 if interval<1 else interval
    auto=data['settings']['auto']=="1"
    #------------------------------------------------------------
    if auto:os.system('node ~/iot/network-manager/dataSend.js')
    time.sleep(interval)
