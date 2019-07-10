from SPIStage import *
from datetime import datetime, date

x = SPIStage(0, 0)
y = SPIStage(0, 1)

home = [3000, 3000]
target = [3360, 3000]

x.move_to_target(home[0])
y.move_to_target(home[1])
time.sleep(1)
x.move_to_target(target[0])
y.move_to_target(target[1])

start_time = time.time()

for i in range(100):
    time.sleep(.001)
    print(str(i) + ':')
    print(x.view_closed_loop_status_and_position())
    print(y.view_closed_loop_status_and_position())

end_time = time.time()
duration = datetime.combine(date.today(), start_time) - datetime.combine(date.today(), end_time)
print(duration)
