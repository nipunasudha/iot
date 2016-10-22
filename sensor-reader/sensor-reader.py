import redis
import time
from random import randint
from datetime import datetime
import json
import RPi.GPIO as GPIO
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

# print ("Read-interval : "+str(readinterval)+" seconds")
#============  GPIO SETUP  =============
btn=14
led=15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
#============== COMMON DEF ================

def datestr():
    output=str(datetime.now().year)[2:]+str(datetime.now().month).zfill(2)+str(datetime.now().day).zfill(2)+str(datetime.now().hour).zfill(2)+str(datetime.now().minute).zfill(2)+str(datetime.now().second).zfill(2)+str(datetime.now().microsecond)[:2].zfill(2)
    return output
#=============== VARIABLES =================
r=redis.StrictRedis(host='localhost',port=6379, db=0)
x=0

print('====================================\n')
print('SENSOR READING SERVICE\n')
print('====================================\n')


#================ MAIN LOOP ================
while True:
    #------------------ Read settings data ----------------------
    data=read()
    readinterval=float(data['settings']['readinterval'])
    sensors=data['sensors']
    #------------------------------------------------------------
    x=x+1
    #-----------------------------------------------
    terminalid="001T"
    timestamp=datestr()
    entrykey=terminalid+datestr()
    value=GPIO.input(btn)*100
    #-----------------------------------------------
    data=[ { "time_stamp":timestamp, "terminal_id":terminalid }, { "id":"01", "value": value} ]
    GPIO.output(led,GPIO.input(btn))
    dataj=json.dumps(data)
    key=timestamp
    r.set(key,dataj)
    print(dataj)
    time.sleep(readinterval)

