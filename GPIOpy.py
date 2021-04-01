
from RPi.GPIO import setmode, setup, output, BCM, OUT, HIGH, LOW
# imports functions from the RPi.GPIO library
from time import sleep

setmode(BCM)
# pins are called by the number on the pi

ledRED = 17
ledGREEN = 16
# red led = pin 17
# green led = pin 16

setup(ledRED, OUT)
setup(ledGREEN, OUT)
# sets led pins as outputs

count = 0
# counter starts at 0

while count < 10:
# until each led has blinked 10 times
	output(ledRED, HIGH)
	output(ledGREEN, LOW)
# turns the red led on and green one off
	sleep (1)
	output(ledRED, LOW)
	output(ledGREEN, HIGH)
# turns the red led off and green one on
	sleep (1)
	count = count + 1
# adds one to the counter
output (ledGREEN, LOW)
# turns off the green led
