# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Based on example by Mark Roberts (mdroberts1243).

This example writes text to the display, and draws a series of squares and a rectangle.
"""

import board
import displayio
import terminalio
from adafruit_display_text import bitmap_label as label
from adafruit_displayio_sh1107 import SH1107, DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297
import time
import adafruit_adxl34x
import digitalio

displayio.release_displays()


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# For I2C
#i2c = board.I2C()  # uses board.SCL and board.SDA
i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)

accelerometer = adafruit_adxl34x.ADXL345(i2c)

# For SPI:
# import busio
# spi_bus = busio.SPI(board.SCK, board.MOSI)
# display_bus = displayio.FourWire(spi_bus, command=board.D6, chip_select=board.D5, reset=board.D9)

# Width, height and rotation for Monochrome 1.12" 128x128 OLED
WIDTH = 128
HEIGHT = 128
ROTATION = 90

# Border width
BORDER = 2

display = SH1107(
    display_bus,
    width=WIDTH,
    height=HEIGHT,
    display_offset=DISPLAY_OFFSET_ADAFRUIT_128x128_OLED_5297,
    rotation=ROTATION,
)

# Make the display context
splash = displayio.Group()
#display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle in black
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw some white squares
small_bitmap = displayio.Bitmap(8, 8, 1)
small_square = displayio.TileGrid(small_bitmap, pixel_shader=color_palette, x=58, y=17)
splash.append(small_square)

medium_bitmap = displayio.Bitmap(16, 16, 1)
medium_square = displayio.TileGrid(
    medium_bitmap, pixel_shader=color_palette, x=71, y=15
)
splash.append(medium_square)

large_bitmap = displayio.Bitmap(32, 32, 1)
large_square = displayio.TileGrid(large_bitmap, pixel_shader=color_palette, x=91, y=28)
splash.append(large_square)

#bottom_bitmap = displayio.Bitmap(110, 50, 1)
#bottom_rectangle = displayio.TileGrid(
#    bottom_bitmap, pixel_shader=color_palette, x=10, y=69
#)
#splash.append(bottom_rectangle)

# Draw some label text
name_text = "Monochrome 1.12in"
name_text_area = label.Label(terminalio.FONT, text=name_text, color=0xFFFFFF, x=8, y=8)
splash.append(name_text_area)
size_text = "128x128"
size_text_area = label.Label(terminalio.FONT, text=size_text, color=0xFFFFFF, x=8, y=25)
splash.append(size_text_area)
oled_text = "OLED"
oled_text_area_x = label.Label(
    terminalio.FONT, text=oled_text, scale=2, color=0xFFFFFF, x=9, y=44
)

oled_text_area_y = label.Label(
    terminalio.FONT, text=oled_text, scale=2, color=0xFFFFFF, x=9, y=64
)

oled_text_area_z = label.Label(
    terminalio.FONT, text=oled_text, scale=2, color=0xFFFFFF, x=9, y=84
)
splash.append(oled_text_area_x)
splash.append(oled_text_area_y)
splash.append(oled_text_area_z)
display.show(splash)

# data = displayio.Group()
# display.show(data)
while True:
    led.value = False
    print("%f %f %f" % accelerometer.acceleration)
    xpos = '{:.2f}'.format(accelerometer.acceleration[0])
    oled_text_area_x.text = xpos
    
    ypos = '{:.2f}'.format(accelerometer.acceleration[1])
    oled_text_area_y.text = ypos
    
    zpos = '{:.2f}'.format(accelerometer.acceleration[2])
    oled_text_area_z.text = zpos
    
    
    time.sleep(0.25)
    led.value = True
    time.sleep(0.025)

