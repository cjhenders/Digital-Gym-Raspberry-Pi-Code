#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#       Hall Effect Sensor
#
# This script tests the sensor on GPIO17.
#
# Author : Matt Hawkins
# Date   : 27/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import RPi.GPIO as GPIO
import time
import datetime
import requests
import urllib
import httplib
import smtplib
from email.mime.text import MIMEText

global last_time

#Define the API endpoint: 
API_ENDPOINT = "http://52.34.141.31:8000/bbb/bike"


def sensorCallback1(channel):
  
	global last_time
	global miss

	miss =0
	if not last_time:
	last_time = 0
 
	# Called if sensor output goes LOW
	current_time = time.time()
	if ((1 / (current_time - last_time)) * 60 < 200) and ((1 / (current_time - last_time)) * 60 > 10):
        # Send Post request and save the response as a response object
        rpm = (1/(current_time - last_time))*60
        print rpm
        data = {"rpm": rpm, "bikeId": "1"}
        try:
            r = requests.post(url = API_ENDPOINT, data = data)
        except requests.exceptions.RequestException as e:
            print "Connection Error"
            if email == False:
                email = True
                msg["Subject"] = "Pi Bike #1 has had a connection error"
                msg["From"] = cjhenders @ gmail.com
                msg["To"] = cjhenders @ gmail.com
                s = smtplib.SMTP("localhost")
                s.sendmail(cjhenders @ gmail.com, [cjhenders @ gmail.com], msg.as_string())
                s.quit
			#extracting response text
			pastebin_url = r.text
			print("the pastebin URL is: %s"%pastebin_url)
			last_time = current_time
  



def main():  
	global miss
	global email
	email = False
	miss = 0
	# Wrap main content in a try block so we can
	# catch the user pressing CTRL-C and run the
	# GPIO cleanup function. This will also prevent
	# the user seeing lots of unnecessary error
	# messages.
  
  
	try:
		# Loop until users quits with CTRL-C
		while True :
			miss+=1
			time.sleep(0.1)
			if miss == 30:

				data = {"rpm": 0,
					"bikeId": "1"}
			try:        
				r = requests.post(url = API_ENDPOINT, data = data)
				email = False
			except requests.exceptions.RequestException as e:
				print "Connection Error"
				if email == False:
					email = True
					msg["Subject"] = "Pi Bike #1 has had a connection error"
					msg["From"] = cjhenders@gmail.com
					msg["To"] = cjhenders@gmail.com
					s = smtplib.SMTP("localhost")
					s.sendmail(cjhenders@gmail.com,[cjhenders@gmail.com],msg.as_string())
					s.quit
			# Send Post request and save the response as a response object
			#extracting response text

			pastebin_url = r.text
		    print("0 Response %s"%pastebin_url)


  except KeyboardInterrupt:
    # Reset GPIO settings
	GPIO.cleanup()
  
# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print "Setup GPIO pin as input"

# Set Switch GPIO as input
GPIO.setup(27 , GPIO.IN)
GPIO.add_event_detect(27, GPIO.FALLING, callback=sensorCallback1)


if __name__=="__main__":
  last_time = 0
  main()
   
