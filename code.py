
from adafruit_circuitplayground import cp
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from sensorlightdisplay import SensorLightDisplay
kbd = Keyboard(usb_hid.devices)

# ---------------------------------- -----
blue = [0, 0, 255]
purple = [204, 122, 245]
orange = [133, 94, 4]

hehe = SensorLightDisplay(0.05)

while True:
    x = cp.acceleration[0]
    if cp.switch == True:
        hehe.advanced_control_feedback(x, blue)
        if cp.button_b:
            kbd.send(Keycode.SPACEBAR)
            hehe.alternate_colour(orange, purple)
        elif cp.button_a:
            kbd.send(Keycode.SPACEBAR)
            hehe.alternate_colour(orange, purple)


