import pygame
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen [width,height]
res = 750
size = [res, res]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

x = res / 2
y = res / 2

xp = 0
yp = 0

numSample = 1
xsum = [res / 2] * numSample
ysum = [res / 2] * numSample
tick = 0

points0 = []
points1 = []

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done == False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        textPrint.print(screen, "Joystick {}".format(i))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for j in range(axes):
            axis = joystick.get_axis(j)
            textPrint.print(screen, "Axis {} value: {:>6.3f}".format(j, axis))
            if j == 0:
                xsum[tick] = axis * res / 2 + res / 2
            if j == 1:
                ysum[tick] = axis * res / 2 + res / 2

        textPrint.unindent()

        button = joystick.get_button(0)
        xp = round(sum(xsum) / numSample)
        yp = round(sum(ysum) / numSample)

        if i == 0:
            pygame.draw.circle(screen, BLACK, [xp, yp], 3)
            if button:
                points0.append([xp, yp])
            else:
                points0 = []

        if i == 1:
            pygame.draw.circle(screen, RED, [xp, yp], 3)
            if button:
                points1.append([xp, yp])
            else:
                points1 = []

        if len(points0) > 1:
            pygame.draw.lines(screen, GREEN, False, points0)
        if len(points1) > 1:
            pygame.draw.lines(screen, BLUE, False, points1)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

    tick += 1
    if tick >= numSample:
        tick = 0

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
