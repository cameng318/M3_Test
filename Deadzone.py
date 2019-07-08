import os
import glob

files = [f for f in glob.glob("/dev/input/by-id/usb-*-event-joystick")]
for f in files:
	os.system("evdev-joystick --evdev " + f + " --deadzone 0 --fuzz 0")
