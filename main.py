from SPIStage import *


x = SPIStage(0,0)
y = SPIStage(0,1)

x.send('<06 1 00001770>\r')
print(x.get())
y.send('<06 1 00001770>\r')
print(y.get())
x.send('<06 1 fffff890>\r')
print(x.get())
y.send('<06 1 fffff890>\r')
print(y.get())
