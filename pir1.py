import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
try:
	print("PIR Module Test (CTRL+C to exit)")
	time.sleep(2)
	print("Ready")
	while True:
		if GPIO.input(PIR_PIN):
			#td=t()
			print("Motion Detected! ",time.asctime(time.gmtime()))
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
