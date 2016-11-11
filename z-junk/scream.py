import time
import RPi.GPIO as GPIO
#============  GPIO SETUP  =============
spk=18
GPIO.setmode(GPIO.BCM)
GPIO.setup(spk,GPIO.OUT)
GPIO.setwarnings(False)
while True:
    GPIO.output(spk,False)
   

