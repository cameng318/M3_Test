import pygame


class Joystick:
    def __init__(self):
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.joystick_name = self.joystick.get_name()

        # Treat hats as 4 buttons
        self.num_buttons = self.joystick.get_numbuttons() + 4
        self.buttons = [0] * self.num_buttons

        self.num_axes = self.joystick.get_numaxes()
        self.axes = [0.0] * self.num_axes

        self.num_hats = self.joystick.get_numhats()
        self.hats = [(0, 0)]

        self.update()

    def update(self):
        for event in pygame.event.get():
            for i in range(self.num_buttons - 4):
                self.buttons[i] = self.joystick.get_button(i)
            for i in range(self.num_axes):
                self.axes[i] = self.joystick.get_axis(i)
            for i in range(self.num_hats):
                self.hats[i] = self.joystick.get_hat(i)
        self.buttons[self.num_buttons - 4] = self.hats[0][1] == 1
        self.buttons[self.num_buttons - 3] = self.hats[0][1] == -1
        self.buttons[self.num_buttons - 2] = self.hats[0][0] == -1
        self.buttons[self.num_buttons - 1] = self.hats[0][0] == 1

    def get_name(self):
        return self.joystick_name

    def get_buttons(self):
        self.update()
        return self.buttons

    def get_axes(self):
        self.update()
        return self.axes

    def get_all(self):
        self.update()
        return [self.buttons, self.axes]
