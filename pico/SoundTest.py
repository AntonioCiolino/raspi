
import wave
import numpy as np
import RPi.GPIO as GPIO
import time



# The GPIO pin the buzzer is connected to
BUZZER_PIN = 17

# Set up the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Open the wav file
wav_file = wave.open("/home/admin/PhotonStaff/thunder2.wav", "rb")

# Extract frames
raw_frames = wav_file.readframes(wav_file.getnframes())


# Convert frames to integers
frames = np.frombuffer(raw_frames, dtype='<i2')

# Normalize to the frequency range of the buzzer
frames = ((frames / np.max(np.abs(frames))) * 31000) + 100  # Assuming the buzzer can handle 2000Hz to 4000Hz

# Create a PWM instance
pwm = GPIO.PWM(BUZZER_PIN, frames[0])

try:
    # Start the PWM
    pwm.start(1)

    # Change the frequency for each frame
    for frame in frames[1:]:
      if (frame > 1):
        pwm.ChangeFrequency(frame)
        print(frame)
      time.sleep(1.0 / wav_file.getframerate())  # This waits for the duration of one frame
        
        
    print ("Complete")
finally:
    # Stop the PWM
    pwm.stop()

    # Clean up the GPIO on exit
    GPIO.cleanup()
