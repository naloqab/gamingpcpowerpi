#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
import sys

seconds = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(3, GPIO.OUT)

closeSwitch = False
openSwitch = True

GPIO.output(3, closeSwitch)
sleep(seconds)
GPIO.output(3, openSwitch)