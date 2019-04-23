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

import os
import json
import time
import serial
import requests
from time import sleep
  
try:
    port = serial.Serial('/dev/ttyS0', 115200)
except serial.serialutil.SerialException:
    log('Serial Error: no connection to /dev/ttyS0 at 115200', 'success')
    sys.exit()
    
port.write(str.encode("Go"))
sleep(0.1)

while True:
    try:
        my_text= port.read() 
        time.sleep(0.1)       
        remaining_bytes = port.in_waiting 
        my_text += port.read(remaining_bytes)
        my_text = my_text.decode()
        data_output = (my_text.strip())
         
    except Exception as e:
        print(str(e))
        pass
    
## Send the data to the FarmBot Web App logs.
#def send_it(data_output):
#	headers = {'Authorization': 'Bearer ' + TOKEN,'content-type': 'application/json'}
#	data = json.dumps({'message': 'Plant Characteristics:' + str(data_output)})
#	response = requests.post('https://my.farmbot.io/api/logs', headers=headers, data=data)
#	print "sent it!"


#def main():
#	get_token()
#	data_output = Run_Routines()
#	send_it(data_output)

def log(message, message_type): #'Send a send_message command to post a log to the Web App.'
 
    requests.post(
        os.environ['FARMWARE_URL'] + 'api/v1/celery_script',
        headers={'Authorization': 'Bearer ' + os.environ['FARMWARE_TOKEN'],
                 'content-type': 'application/json'},
        data=json.dumps({
            'kind': 'send_message',
            'args': {
                'message': message,
                'message_type': message_type}}))	
if __name__ == '__main__':
        log("Started Program", "success")
