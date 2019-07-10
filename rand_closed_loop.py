from SPIStage import *
import random

x = SPIStage(0, 0)
y = SPIStage(0, 1)

home = [4614, 1457]

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(.5)
print('before:')
print(x.view_closed_loop_status_and_position())
print(y.view_closed_loop_status_and_position())

for i in range(10):
    x.move_to_target(random.randrange(-6000, 6000, 1))
    y.move_to_target(random.randrange(-6000, 6000, 1))
    time.sleep(.5)

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(.5)

print('after:')
print(x.view_closed_loop_status_and_position())
print(y.view_closed_loop_status_and_position())