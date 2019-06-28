from SPIStage import *


x = SPIStage(0,0)
y = SPIStage(0,1)

x.send('<08 00001770>\r')
print(x.get())
y.send('<08 00001770>\r')
print(y.get())

time.sleep(2)

x.send('<08 fffff890>\r')
print(x.get())
y.send('<08 fffff890>\r')
print(y.get())
