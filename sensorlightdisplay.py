from adafruit_circuitplayground import cp
import time
import usb_hid
from adafruit_circuitplayground import cp
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices)
cp.pixels.auto_write = False
class SensorLightDisplay:
    def __init__(self, brightness):
        self.pixels_off_state = [0, 0, 0]
        self.pixels_amount = len(cp.pixels)
        self.halfway_point = self.pixels_amount // 2
        cp.pixels.brightness = brightness

    def advanced_control_feedback(self,acceleration_x, colour):
        acceleration_peak = 9.81
        flipped_x = 0
        if flipped_x < acceleration_peak:
            if acceleration_x < -3:
                for pixel in range(self.halfway_point, self.pixels_amount):
                    cp.pixels[pixel] = colour
                kbd.send(Keycode.LEFT_ARROW)
                cp.pixels.show()
            elif acceleration_x > 3:
                for pixel in range(self.halfway_point):
                    cp.pixels[pixel] = colour
                kbd.send(Keycode.RIGHT_ARROW)
                cp.pixels.show()
            else:
                cp.pixels.fill(self.pixels_off_state)

    def alternate_colour(self, colour_1, colour_2):
         for pixel in range(self.pixels_amount ):
            if pixel % 2 == 0:
                cp.pixels[pixel] = colour_1
            else:
                cp.pixels[pixel] = colour_2
            cp.pixels.show()
            time.sleep(0.05)
            cp.pixels[pixel] = self.pixels_off_state




