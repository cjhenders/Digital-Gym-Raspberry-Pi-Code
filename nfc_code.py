"""
Code to read RFID Tags for Rasp Pi

Carl Henderson Feb 2017
"""

import nfc
import time
import datetime
import requests
import urllib
import httplib


def connected(tag):
    print(tag);
    return False


clf = nfc.ContactlessFrontend('usb')

while True:
    API_ENDPOINT = API_ENDPOINT = "http://52.34.141.31:8000/bbb/addsession"
    API_KEY = "ashu1234"

    tag = clf.connect(rdwr={'on-connect': connected})
    data = {"tag": tag, "bikeId": 1}
    try:
        r = requests.post(url=API_ENDPOINT, data=data)
    except requests.exceptions.RequestException as e:
        print e



    # extracting response text
    pastebin_url = r.text
    print("the pastebin URL is: %s" % pastebin_url)
