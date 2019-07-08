import os

os.system("evdev-joystick --evdev /dev/input/by-id/usb-*-event-joystick --deadzone 0 --fuzz 0")