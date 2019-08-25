from SPIStage import *

x = SPIStage(0, 0)
print(x.select_open_loop_drive_mode())
print(x.select_closed_loop_drive_mode())