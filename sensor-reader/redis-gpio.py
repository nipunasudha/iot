import redis
import time
from random import randint
from datetime import datetime
import json
import RPi.GPIO as GPIO

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
    time.sleep(0.5)

