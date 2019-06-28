import time
import spidev

bus = 0

device = 0

spi = spidev.SpiDev()

sip.open(bus, device)

spi.max_speed_hz = 2000000

spi.mode = 0

reply = spi.xfer2([0x01])

print(reply)