from SPIStage import *

x = SPIStage(0, 0)
y = SPIStage(0, 1)

x.send('<87 4>\r')
print(x.get())
y.send('<87 4>\r')
print(y.get())
