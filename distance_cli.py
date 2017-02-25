# Copyright 2017 Bas van der Sluis
# For instructions see https://www.youtube.com/channel/UC0fmlVYfLz9oYDjRNuN9k3w

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

# Pins connected to the HC-SR04 sensor
iTriggerPin = 21
iEchoPin    = 20

GPIO.setup(iTriggerPin, GPIO.OUT)
GPIO.setup(iEchoPin, GPIO.IN)

GPIO.output(iTriggerPin, False)
time.sleep(0.5)

while True:
	GPIO.output(iTriggerPin, True)
	time.sleep(0.0001)
	GPIO.output(iTriggerPin, False)

	while GPIO.input(iEchoPin) == 0:
		pass
	fPulseStart = time.time()

	while GPIO.input(iEchoPin) == 1:
		pass
	fPulseEnd = time.time()

	fPulseDuration = fPulseEnd - fPulseStart

	fDistance = round((fPulseDuration * 17150), 2)

	print "Distance:", fDistance, "cm."

	time.sleep(0.5)

GPIO.cleanup()
