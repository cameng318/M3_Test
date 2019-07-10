from SPIStage import *
import random

x = SPIStage(0, 0)
y = SPIStage(0, 1)

home = [4614, 1457]
target = [6000,6000]
delay = 0.5

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(delay)

print('before:')
print(x.view_closed_loop_status_and_position())
print(y.view_closed_loop_status_and_position())

for i in range(10):
    target = [random.randrange(0, 12000, 1), random.randrange(0, 12000, 1)]
    x.move_to_target(target[0])
    time.sleep(delay)
    print(str(i) + ':')
    print(x.view_closed_loop_status_and_position())
    print(y.view_closed_loop_status_and_position())

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(delay)

print('after:')
print(x.view_closed_loop_status_and_position())
print(y.view_closed_loop_status_and_position())