#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)

closeSwitch = False
openSwitch = True

GPIO.output(3, closeSwitch)
sleep(1)
GPIO.output(3, openSwitch)
