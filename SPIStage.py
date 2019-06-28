import time
import spidev


class SPIStage:
    def __init__(self, bus, device):
        self.axis = spidev.SpiDev()
        self.axis.open(bus, device)
        self.axis.max_speed_hz = 1000000
        self.axis.mode = 1

    def send(self, msg):
        msg = [ord(x) for x in msg]
        self.axis.writebytes(msg)
        time.sleep(.00006)

    def get(self):
        reply = self.axis.readbytes(31)
        reply = ''.join([chr(x) for x in reply]).strip('\x01')
        time.sleep(.00006)
        return reply

    def read_the_firmware_version(self):
        self.send('<01>\r')
        return self.get()

    def halt_the_motor(self):
        self.send('<03>\r')
        if self.get() == '<03>\r':
            return 0
        else:
            return -1
