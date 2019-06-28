from SPIStage import *

x = SPIStage(0, 0)
y = SPIStage(0, 1)

x.move_to_target(6000)
time.sleep(2)
x.move_to_target(-6000)