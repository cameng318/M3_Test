from SPIStage import *


x = SPIStage(0,0)
y = SPIStage(0,1)

print(x.read_the_firmware_version())
print(y.read_the_firmware_version())
print(x.halt_the_motor())
print(y.halt_the_motor())