from Joystick import *
from config import *
from StageSPI import *
from StageI2C import *
import pygame

# Clear the Linux built-in deadzone
exec(open("Deadzone.py").read())

# Initialize all 3 stages
x = StageSPI(0, 0)
y = StageSPI(0, 1)
z = StageI2C(1, 0x40)

# Initialize pygame and joystick functions
pygame.init()
joystick = Joystick()
buttons, axes = joystick.get_all()

# Declare default home position and current position
home = [6000, 6000, 6000]
position = [6000, 6000, 6000]

# Declare default sensitivity level for x and y axes
sensitivity_level = 0

# Declare if both x and y axes has been homed
# Threshold for homing declared in config.py
Homed = True


def clamp(num):
    if num > 12000:
        return 12000
    elif num < 0:
        return 0
    else:
        return int(num)


while True:
    buttons_old = buttons[:]
    buttons, axes = joystick.get_all()
    buttons_change = [x - y for x, y in zip(buttons, buttons_old)]

    if buttons_change[18] == 1 or buttons_change[0] == 1:
        sensitivity_level += 1
        if sensitivity_level >= len(Sensitivity):
            sensitivity_level = len(Sensitivity) - 1
        home[0] = clamp(position[0] - axes[0] * Sensitivity[sensitivity_level])
        home[1] = clamp(position[1] + axes[1] * Sensitivity[sensitivity_level])

    if buttons_change[19] == 1 or buttons_change[0] == -1:
        sensitivity_level -= 1
        if sensitivity_level < 0:
            sensitivity_level = 0
        home[0] = clamp(position[0] - axes[0] * Sensitivity[sensitivity_level])
        home[1] = clamp(position[1] + axes[1] * Sensitivity[sensitivity_level])

    if buttons_change[16] == 1:
        position[2] = clamp(position[2] + Z_Sensitivity)

    if buttons_change[17] == 1:
        position[2] = clamp(position[2] - Z_Sensitivity)

    if buttons_change[2] == 1:
        home[0] = position[0]
        home[1] = position[1]
        Homed = False

    if Homed:
        position = [clamp(home[0] + axes[0] * Sensitivity[sensitivity_level]),
                    clamp(home[1] - axes[1] * Sensitivity[sensitivity_level]),
                    position[2]]
    else:
        if (abs(axes[0]) < Home_threshold) and (abs(axes[1]) < Home_threshold):
            Homed = True

    print(position, sensitivity_level,
          x.move_to_target(position[0]),
          y.move_to_target(position[1]),
          z.move_to_target(position[2]))
