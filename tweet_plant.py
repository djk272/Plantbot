#!/usr/bin/env python #Imports
import serial
import time
import numpy
import ftplib
import tweepy, time, sys
###~~This code takes the temperature data monitoring a plant from a Thermistor on an Arduino UNO.~~###
###~~The temperatures are sent to this Python code and tweets the plants status every 5 mins through Twitter API.~~###

#enter the corresponding information from your Twitter application: CONSUMER_KEY = 'bzkwimwyqTYB5BeqtCTxx1DsS'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'PQJl8s9yJHcIYCHPXj5GFdUMhcnIZe5UnitEYF0XAkWhdOLuTF'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '803050766235643904- POW44BkBVoY9pkkMKpfncgCrBM5TexW'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'BEG5p5XEKqvDTaTQTS3PwNWoXMxOp3JTTqyO0NRCecJiI'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Open serial port
ser = serial.Serial('/dev/cu.usbmodem1411', 9600) #read data from serial port of computer (varies for each computer)
time.sleep(1)
ser.flush

# Read some data
for i in range(2): #removes any bad data from inital read
ser.readline()

#Main loop while(True):
#Read data and convert to temperature
temp = ((int(ser.readline())*0.004882814)-0.5)*100 print temp
######################################################################

################################
if temp < 22: #if the temperature from the sensor is below this number the plant is ok, if 10C you'd know
Tw1 = "Im okay atm" print Tw1
tweet = str(temp) + " C: - " + Tw1 #Tweet the temperature in Celcius and a descriptive comment
api.update_status(tweet)
time.sleep(300) #Delay, tweet every 5 minutes ###################################################################### ################################

if temp >= 26: #if the temperature from the sensor is greater than or equal to this number the plant is a little warm
Tw2 = "Bruhh its lit" print Tw2
tweet = str(temp) + " C: - " + Tw2 #Tweet the temperature in Celcius and a descriptive comment
api.update_status(tweet)
time.sleep(300) #Delay, tweet every 5 minutes ###################################################################### ################################

if temp > 30: #if the temperature from the sensor is greater than this number the plant is getting too hot
Tw3 = "This is fine [sweats, internal screaming]" print Tw3
tweet = str(temp) + " C: - " + Tw1 #Tweet the temperature in Celcius and a descriptive comment
api.update_status(tweet)
time.sleep(300) #Delay, tweet every 5 minutes
