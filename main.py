from SPIStage import *
import random

x = SPIStage(0, 0)
y = SPIStage(0, 1)

while 1:
    x.move_to_target(random.randrange(-6000, 6000, 1))
    y.move_to_target(random.randrange(-6000, 6000, 1))
    time.sleep(2)
