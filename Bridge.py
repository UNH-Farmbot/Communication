#!/usr/bin/env python

""" UNHFarmbot PhenotypeApp

#=======================================================================
#
#
#         ~~~~~~~~~~~~~~~   PhenotypeApp   ~~~~~~~~~~~~~~~    
#
#                        UNHFarmbot Farmware        
#
#=======================================================================
# Written by: Alfred Odierno, Amadou Tall, Issam Benabdelkrim
#
# Created: Ver. 0.1.0 12/6/18
# Updated: ver. 1.0.0  4/12/19 by Amadou Tall
#
#-----------------------------------------------------------------------
# This program is designed to work in conjunction with Farmware created 
# for the FarmBot web-app. 
#
# The Phenotype Farmware will take a picture of a plant being managed by 
# Farmbot. The image will be analysed and flower count, flower size, and
# canopy area will be generated. This data will be outputed to the 
# web-app via Logs. When the Farmware sequence is run, a start command 
# is sent from the Farmbot's raspberry pi to the Image processing Pi 
# via serial signal lines. Data generated on the IPpi is returned the 
# same way.
#------------------------------------------------------------------------"""


import json
import time
import serial
from time import sleep

def printheader():
    print("")
    print("")
    print('%s%s'%(" " * 6,
                  "    Leaf Area       Bloom Size   Bloom Color   Bloom Count"))
    print('%s%s'%(" " * 6,
                  "      (cm^2)          (in)                      (#/plant)"))
    print('%s%s'%(" " * 6, "-" * 60))

try:
    port = serial.Serial('/dev/ttyS0', 115200)
except serial.serialutil.SerialException:
    print
    print("Serial Error: no connection to /dev/ttyS0 at 115200")
    print
    sys.exit()
    
port.write(str.encode("Go"))
sleep(0.1)


printheader()


while True:
    try:
        my_text= port.read() 
        time.sleep(0.1)       
        remaining_bytes = port.in_waiting 
        my_text += port.read(remaining_bytes)
        my_text = my_text.decode()
        data_output = (my_text.strip())
        new_file = open("/home/pi/Messi2.txt", "w")
        new_file.write(data_output)
        print(data_output)
        new_file.close
            
    except Exception as e:
        print(str(e))
        pass

    if __name__ == '__main__':
        log("Started Program", "success")
     #   install_and_import('serial')
        log("Ending Program", "success")
       # initiate()
