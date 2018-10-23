# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BCM)

# GPIO.setwarnings(False)

# GPIO.setup(3, GPIO.OUT)

# closeSwitch = False
# openSwitch = True

# GPIO.output(3, closeSwitch)
# sleep(1)
# GPIO.output(3, openSwitch)

import os
os.system("python3 /home/pi/code/GamingPCPowerButton.py 1")
