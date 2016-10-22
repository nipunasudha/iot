import os
import time
print("===========================================")
print("DATA UPLOADER LAUNCHER SERVICE\n")
while 1:
    os.system('node ~/iot/network-manager/dataSend.js')
    time.sleep(15)
