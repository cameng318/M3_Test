""" Linux has a built-in 5% deadzone for joysticks. This script only removes deadzones for evdev interface.
    The deadzone resets once the joystick is unplugged and plugged back in.
"""
import os
import glob

files = [f for f in glob.glob("/dev/input/by-id/usb-*-event-joystick")]
for f in files:
    os.system("evdev-joystick --evdev " + f + " --deadzone 0 --fuzz 0")
