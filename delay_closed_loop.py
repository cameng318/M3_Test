from SPIStage import *
import random

x = SPIStage(0, 0)
y = SPIStage(0, 1)

home = [4614, 1457]
target = [4714,1457]

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(1)

for i in range(100):
    x.move_to_target(target[0])
    y.move_to_target(target[1])
    time.sleep(i/100)
    print(str(i) + ':')
    print(x.view_closed_loop_status_and_position())
    print(y.view_closed_loop_status_and_position())
