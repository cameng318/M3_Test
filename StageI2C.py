from Stage import *
import smbus
import time


class StageI2C(Stage):
    def __init__(self, bus, address):
        """ Initialize I2C communication. """
        Stage.__init__(self)
        self.bus = smbus.SMBus(bus)
        self.address = address

        # Calibrate frequency for optimal performance
        self.frequency_calibration()

    def send(self, msg):
        """ Send message to the I2C device. """
        # Format the message to ASCII.
        message = [ord(x) for x in msg]

        # Attempt to send message through I2C communication.
        # The communication may fail at times due to latency. Thus use try and except.
        try:
            self.bus.write_i2c_block_data(self.address, 0, message)
            time.sleep(.00006)
        except I2CError:
            pass

    def get(self):
        """ Receive message from the I2C device. """
        # Attempt to receive message through I2C communication.
        # The communication may fail at times due to latency. Thus use try and except.
        reply = ''
        try:
            reply = self.bus.read_i2c_block_data(self.address, 0)
            time.sleep(.00006)
        except OSError:
            pass

        # Join the bytes together and strip off the empty signs
        message = ''.join([chr(x) for x in reply]).strip('\x01')

        return message
