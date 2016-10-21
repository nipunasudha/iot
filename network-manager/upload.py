import os
import time
print("DATA UPLOADER LAUNCHER SERVICE\n")
while 1:
    os.system('lxterminal -l -e "node ~/iot/network-manager/dataSend.js"')
    time.sleep(15)
