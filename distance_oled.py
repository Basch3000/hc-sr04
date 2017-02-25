# Copyright 2017 Bas van der Sluis
# For instructions see https://www.youtube.com/channel/UC0fmlVYfLz9oYDjRNuN9k3w

import RPi.GPIO as GPIO
import time

# Can't set the mode to board here, because the Adafruit-GPUI library automatically
# sets the mode to BCM
#GPIO.setmode(GPIO.BOARD)

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Pins for the HC-SR04 sensor
iTriggerPin = 21
iEchoPin    = 20

# Pins 23 and 24 are connected to the OLED display
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, dc=23, spi=SPI.SpiDev(0, 0, max_speed_hz=8000000))

GPIO.setup(iTriggerPin, GPIO.OUT)
GPIO.setup(iEchoPin, GPIO.IN)

GPIO.output(iTriggerPin, False)
time.sleep(0.5)

disp.begin()
font = ImageFont.truetype('NovaMono.ttf', 26)

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

	#disp.clear()
	#disp.display()

	image = Image.new('1', (128, 64))
	draw = ImageDraw.Draw(image)

	draw.text((2, -2),  'Distance', font=font, fill=255)
	draw.text((2, 28), str(fDistance) + "cm.",  font=font, fill=255)

	disp.image(image)
	disp.display()

	time.sleep(0.5)

GPIO.cleanup()
