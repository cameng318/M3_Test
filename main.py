from Joystick import *
from config import *
from StageSPI import *
from StageI2C import *
import pygame

# Clear the Linux built-in joystick deadzone
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
home = [DefaultHome, DefaultHome, DefaultHome]
position = [DefaultHome, DefaultHome, DefaultHome]

# Declare default sensitivity level for x and y axes
sensitivity_level = 0

# Declare if both x and y axes has been homed
# Threshold for homing declared in config.py
Homed = True


def clamp(num):
    """ Clamp the number to an acceptable range of the linear stages. """
    if num > AbsMax:
        return AbsMax
    elif num < AbsMin:
        return AbsMin
    else:
        return int(num)


while True:
    """ Loop forever. """
    # Record previous states of the buttons.
    buttons_old = buttons[:]

    # Update the states for buttons and axes
    buttons, axes = joystick.get_all()

    # Compute the changes in buttons.
    # 1 means the button is just pressed.
    # -1 means the button is just released.
    # 0 means the button is unchanged.
    buttons_change = [x - y for x, y in zip(buttons, buttons_old)]

    # Sensitivity up
    if buttons_change[HAT_RIGHT] == 1 or buttons_change[FRONT_TRIGGER] == 1:
        sensitivity_level += 1
        if sensitivity_level >= len(Sensitivity):
            sensitivity_level = len(Sensitivity) - 1
        home[0] = clamp(position[0] - axes[0] * Sensitivity[sensitivity_level])
        home[1] = clamp(position[1] + axes[1] * Sensitivity[sensitivity_level])

    # Sensitivity down
    if buttons_change[HAT_LEFT] == 1 or buttons_change[FRONT_TRIGGER] == -1:
        sensitivity_level -= 1
        if sensitivity_level < 0:
            sensitivity_level = 0
        home[0] = clamp(position[0] - axes[0] * Sensitivity[sensitivity_level])
        home[1] = clamp(position[1] + axes[1] * Sensitivity[sensitivity_level])

    # Z axis up
    if buttons_change[HAT_UP] == 1:
        position[2] = clamp(position[2] + Z_Sensitivity)

    # Z axis down
    if buttons_change[HAT_DOWN] == 1:
        position[2] = clamp(position[2] - Z_Sensitivity)

    # Set home for x and y axes
    if buttons_change[LEFT_BUTTON] == 1:
        home[0] = position[0]
        home[1] = position[1]
        Homed = False

    # Reset home for x and y axes
    if buttons_change[DOWN_BUTTON] == 1:
        home[0] = DefaultHome
        home[1] = DefaultHome

    # Update current position
    if Homed:
        position = [clamp(home[0] + axes[0] * Sensitivity[sensitivity_level]),
                    clamp(home[1] - axes[1] * Sensitivity[sensitivity_level]),
                    position[2]]
    else:
        if (abs(axes[0]) < Home_threshold) and (abs(axes[1]) < Home_threshold):
            Homed = True

    # Send current position to the linear stages
    print('Current Position: ', position,
          'Sensitivity: ', sensitivity_level,
          'Messages: ',
          x.move_to_target(position[0]),
          y.move_to_target(position[1]),
          z.move_to_target(position[2]),
          x.view_closed_loop_status_and_position())