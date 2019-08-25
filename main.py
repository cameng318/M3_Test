from Joystick import *
from config import *
from SPIStage import *
import pygame
import time

x = SPIStage(0, 0)
y = SPIStage(0, 1)

pygame.init()
joystick = Joystick()
buttons, axes = joystick.get_all()

home = [6000, 6000, 6000]
position = [6000, 6000, 6000]
sensitivity_level = 0
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
        if (abs(axes[0]) < 0.05) and (abs(axes[1]) < 0.05):
            Homed = True

    print(position, sensitivity_level, x.get(), y.get())
    x.move_to_target(position[0])
    y.move_to_target(position[1])

    #time.sleep(.01)