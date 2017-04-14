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

# Define the API endpoint:
API_ENDPOINT = "http://52.34.141.31:8000/bbb/bike"


def sensorCallback1(channel):
    global last_time
    global miss

    miss = 0
    if not last_time:
        last_time = 0

    current_time = time.time()
    if ((1 / (current_time - last_time)) * 60 < 200) and ((1 / (current_time - last_time)) * 60 > 10):
        rpm = (1 / (current_time - last_time)) * 60
        print rpm
        post_data = {"rpm": rpm, "bikeId": "1"}
        try:
            r = requests.post(url=API_ENDPOINT, data=post_data)
        except request.exceptions.RequestException as e:
            print e

        last_time = current_time


def main():
    global miss

    miss = 0

    try:
        while True:
            miss += 1
            time.sleep(0.1)
            if miss == 30:
                data = {"rpm": 0, "bikeId": "1"}
            try:
                r = requests.post(url=API_ENDPOINT, data=data)
            except request.exceptions.RequestException as e:
                print e

            print("0 Response Posted")

    except KeyboardInterrupt:
        GPIO.cleanup()


GPIO.setmode(GPIO.BCM)

print "Setup of GPIO pin as Input for RPM Sensor"

# Set switch GPIO as input

GPIO.setup(27, GPIO.IN)
GPIO.add_event_detect(27, GPIO.FALLING, callback=sensorCallback1)

if __name__ == "__main__":
    last_time = 0
    main()
