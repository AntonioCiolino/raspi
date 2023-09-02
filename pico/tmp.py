import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
# we'll have GPIO package deal with BCM (Broadcom GPIO 00..nn numbers)
# rather than BOARD (Raspberry Pi board numbers)
GPIO.setup(13, GPIO.OUT)  # set BCM pin 13 to output a signal
backlight_pin = GPIO.PWM(13, 500)  # set BMC pin 13 to pulse signal waves high(on)/low(off) modulated at 500Hz frequency (500 times a second)
backlight_pin.start(100)  # for each pulse cycle, the signal should be high (on duty) for 100% of the cycle; duty-cycle = 100%
backlight_pin.ChangeDutyCycle(50)  # for each pulse cycle, the signal should be high for 50% of the cycle; duty-cycle = 50%

backlight_pin.stop()
import signal
import RPi.GPIO as GPIO

print("""buttons.py - Detect which button has been pressed

This example should demonstrate how to:
1. set up RPi.GPIO to read buttons,
2. determine which button has been pressed

Press Ctrl+C to exit!

""")

# The buttons on Pirate Audio are connected to pins 5, 6, 16 and 24
# Boards prior to 23 January 2020 used 5, 6, 16 and 20 
# try changing 24 to 20 if your Y button doesn't work.
BUTTONS = [5, 6, 16, 24]

# These correspond to buttons A, B, X and Y respectively
LABELS = ['A', 'B', 'X', 'Y']

# Set up RPi.GPIO with the "BCM" numbering scheme
GPIO.setmode(GPIO.BCM)

# Buttons connect to ground when pressed, so we should set them up
# with a "PULL UP", which weakly pulls the input signal to 3.3V.
GPIO.setup(BUTTONS, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# "handle_button" will be called every time a button is pressed
# It receives one argument: the associated input pin.
def handle_button(pin):
    label = LABELS[BUTTONS.index(pin)]
    print("Button press detected on pin: {} label: {}".format(pin, label))


# Loop through out buttons and attach the "handle_button" function to each
# We're watching the "FALLING" edge (transition from 3.3V to Ground) and
# picking a generous bouncetime of 100ms to smooth out button presses.
for pin in BUTTONS:
    GPIO.add_event_detect(pin, GPIO.FALLING, handle_button, bouncetime=100)

# Finally, since button handlers don't require a "while True" loop,
# we pause the script to prevent it exiting immediately.
signal.pause()
