from SPIStage import *
import random

x = SPIStage(0, 0)
y = SPIStage(0, 1)

home = [4614, 1457]

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(.5)

for x in range(10):
    x.move_to_target(random.randrange(-6000, 6000, 1))
    y.move_to_target(random.randrange(-6000, 6000, 1))
    time.sleep(.5)

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(.5)