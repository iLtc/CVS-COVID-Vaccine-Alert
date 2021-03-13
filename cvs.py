from datetime import datetime
import random
import requests
import time

STATE='STATE NAME'
TOKEN='PUSHOVER TOKEN'
USER='PUSHOVER USER'

while True:
    r = requests.get('https://www.cvs.com/immunizations/covid-19-vaccine')
    
    text = "At this time, all appointments in {} are booked.".format(STATE)
    
    if text in r.text:
        print("{}: Not Available".format(datetime.now()))
        
        time.sleep(random.randint(300, 600))
        
    
    else:
        print("{}: Available Now!".format(datetime.now()))
        
        payload = {
            'token': TOKEN, 
            'user': USER,
            'message': 'CVS Vaccine Available Now!'
        }
        
        s = requests.post("https://api.pushover.net/1/messages.json", data=payload)
        
        print("{}: Message Sent, {}".format(datetime.now(), s.text))
        
        time.sleep(1800)
        
        