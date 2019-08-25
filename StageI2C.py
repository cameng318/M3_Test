from Stage import *
import smbus
import time


class I2CError(Exception):
    """I2C Communication Error"""
    pass


class StageI2C(Stage):
    def __init__(self, bus, address):
        Stage.__init__(self)
        self.bus = smbus.SMBus(bus)
        self.address = address

    def send(self, msg):
        message = [ord(x) for x in msg]
        try:
            self.bus.write_i2c_block_data(self.address, 0, message)
        except I2CError:
            pass
        time.sleep(.00006)

    def get(self):
        try:
            reply = self.bus.read_i2c_block_data(self.address, 0)
        except I2CError:
            reply = ''
        message = ''.join([chr(x) for x in reply]).strip('\x01')
        time.sleep(.00006)
        return message
