import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
print("LED ON")
GPIO.output(17, GPIO.HIGH)
time.sleep(3)
print("LED OFF")
GPIO.output(17, GPIO.LOW)
