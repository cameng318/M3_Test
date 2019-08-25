from SPIStage import *
import time

x = SPIStage(0, 0)
#print(x.select_closed_loop_drive_mode())
#print(x.move_to_target(6000))
#time.sleep(2)
print(x.select_open_loop_drive_mode())
print(x.set_the_open_loop_mode_speed(0))
time.sleep(1)
print(x.move_the_motor_in_timed_open_loop_steps(0, 0, 0, 0))
time.sleep(10)
print(x.select_closed_loop_drive_mode())
