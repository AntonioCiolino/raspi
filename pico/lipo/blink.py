import board
import digitalio
import time
import audiocore
import audiomp3
import audiobusio
import audiopwmio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

audio = audiobusio.I2SOut(board.GP27, board.GP28, board.GP22)

audiopwm = audiopwmio.PWMAudioOut(board.GP0)


wave_file = open("treefall_16bit.wav", "rb")
wav = audiocore.WaveFile(wave_file)
#audio.play(wav)
audiopwm.play(wav)

while audiopwm.playing:
    time.sleep(0.01)

mp3 = audiomp3.MP3Decoder(open("magic-6976.mp3", "rb"))
#audio.play(mp3)
audiopwm.play(mp3)

while audiopwm.playing:
    pass
    
audiopwm.stop()