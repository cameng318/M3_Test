from Stage import *
import time
import spidev


class StageSPI(Stage):
    def __init__(self, bus, device):
        """ Initialize SPI communication"""
        Stage.__init__(self)
        self.axis = spidev.SpiDev()
        self.axis.open(bus, device)
        self.axis.max_speed_hz = 1000000
        self.axis.mode = 1

    def send(self, msg):
        message = [ord(x) for x in msg]
        self.axis.writebytes(message)
        time.sleep(.00006)

    def get(self):
        reply = self.axis.readbytes(35)
        message = ''.join([chr(x) for x in reply]).strip('\x01')
        time.sleep(.00006)
        return message
