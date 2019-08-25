import pygame


class Joystick:
    def __init__(self):
        # Initialize joysick in pygame. Default to use joystick 0.
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        # Get the name of the joystick.
        self.joystick_name = self.joystick.get_name()

        # Initialize the buttons.
        # Use the first hat as buttons. Thus extra 4 buttons.
        self.num_buttons = self.joystick.get_numbuttons() + 4
        self.buttons = [0] * self.num_buttons

        # Initialize the axes.
        self.num_axes = self.joystick.get_numaxes()
        self.axes = [0.0] * self.num_axes

        # Initialize the hats.
        self.num_hats = self.joystick.get_numhats()
        self.hats = [(0, 0)]

        # Acquire initial values from the joystick.
        self.update()

    def update(self):
        """ Refresh the values for buttons, axes and hats.
            The values for the first hat are appended to the buttons as 4 buttons.
        """
        for event in pygame.event.get():
            for i in range(self.num_buttons - 4):
                self.buttons[i] = self.joystick.get_button(i)
            for i in range(self.num_axes):
                self.axes[i] = self.joystick.get_axis(i)
            for i in range(self.num_hats):
                self.hats[i] = self.joystick.get_hat(i)

        # Append the first hat to the buttons in the sequence of up, down, left and right.
        self.buttons[self.num_buttons - 4] = self.hats[0][1] == 1
        self.buttons[self.num_buttons - 3] = self.hats[0][1] == -1
        self.buttons[self.num_buttons - 2] = self.hats[0][0] == -1
        self.buttons[self.num_buttons - 1] = self.hats[0][0] == 1

    def get_name(self):
        """ Return the name of the joystick. """
        return self.joystick_name

    def get_all(self):
        """ Return the current values for buttons and axes.
            The values for the first hat are appended to the buttons as 4 buttons.
        """
        self.update()
        return [self.buttons, self.axes]

    # Unused Functions
    """
    def get_buttons(self):
        self.update()
        return self.buttons

    def get_axes(self):
        self.update()
        return self.axes
    """
