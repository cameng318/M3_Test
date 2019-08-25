from SPIStage import *
import smbus


class I2CStage(SPIStage):
    def __init__(self, bus, address):
        self.bus = smbus.SMBus(bus)
        self.address = address

    def send(self, msg):
        message = [ord(x) for x in msg]
        try:
            self.bus.write_i2c_block_data(self.address, 0, message)
        except:
            pass
        time.sleep(.00006)

    def get(self):
        try:
            reply = self.bus.read_i2c_block_data(self.address, 0)
        except:
            pass
        message = ''.join([chr(x) for x in reply]).strip('\x01')
        time.sleep(.00006)
        return message
