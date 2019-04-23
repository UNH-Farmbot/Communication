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
from farmware_tools import device

#device.log(message='Plant Charact.:', message_type='success', channels=['toast']) 

#def get_token():
# Inputs:
#	global EMAIL
#	EMAIL = input("FarmBot Email: ")
#	global PASSWORD
#	PASSWORD = input("WebApp Password: ")
# Get your FarmBot Web App token.
#	headers = {'content-type': 'application/json'}
#	user = {'user': {'email': EMAIL, 'password': PASSWORD}}
#	payload = json.dumps(user)
#	response = requests.post('https://my.farmbot.io/api/tokens',headers=headers, data=payload)
#	global TOKEN
#	TOKEN = response.json()['token']['encoded']

# Send "Go" command to image processing Raspberry Pi
def Cmd():
	try:
		port = serial.Serial('/dev/ttyS0', 115200)
		port.write(str.encode("Go"))
		sleep(0.1)
			
	except serial.serialutil.SerialException:
		device.log('Serial Error: no connection to /dev/ttyS0 at 115200', 'success')
		sys.exit()
    
# Receive data through serial  
#def Rcv():
#	while True:
#		device.log(message='Plant Charact.:', message_type='success', channels=['toast'])
#		try:
#			my_text= port.read() 
#			time.sleep(0.1)
			
#			remaining_bytes = port.in_waiting 
#			my_text += port.read(remaining_bytes)
#			my_text = my_text.decode()
#			data_output = (my_text.strip())
#			return(data_output)
			

#		except Exception as e:
#			print(str(e))
#			pass

# Send plant characteristics to log    
def display(100):
	headers = {'Authorization': 'Bearer ' + TOKEN,'content-type': 'application/json'}
	data = json.dumps({'message': 'Plant Characteristics:' + str(100)})
	response = requests.post('https://my.farmbot.io/api/logs', headers=headers, data=data)
	print "Data sent"
	device.log(message='Plant Charact.:', message_type='success', channels=['toast'])		

def main():
	 
#	get_token()
	Cmd()
#  	data_output = Rcv()
#	display(data_output)
	
if __name__ == '__main__':
	main()
      
      
