import time
import spidev

bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 1000000
spi.mode = 1

def send(msg):
    msg = [ord(x) for x in msg]
    spi.writebytes(msg)
    time.sleep(.00006)

def get():
    reply = spi.readbytes(31)
    reply = ''.join([chr(x) for x in reply]).strip('\x01')
    time.sleep(.00006)
    return reply

send('<08 00001770>\r')
print(get())

time.sleep(2)

send('<08 fffff890>\r')
print(get())
