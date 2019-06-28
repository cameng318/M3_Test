import time
import spidev

bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 2000000
spi.mode = 0
msg = [0x01]
print(msg)
reply = spi.xfer2(msg)
print(reply)