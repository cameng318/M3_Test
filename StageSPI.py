from Stage import *
import spidev


class StageSPI(Stage):
    def __init__(self, bus, device):
        """ Initialize SPI communication. """
        Stage.__init__(self)
        self.axis = spidev.SpiDev()
        self.axis.open(bus, device)
        self.axis.max_speed_hz = 1000000
        self.axis.mode = 1

        # Calibrate frequency for optimal performance
        self.frequency_calibration()

    def send(self, msg):
        """ Send message to the SPI device. """
        # Format the message to ASCII.
        message = [ord(x) for x in msg]

        self.axis.writebytes(message)

    def get(self):
        """ Get message from the SPI device. """
        # Receive 35 bytes from the device. The longest message from the M3 linear stage should be 32 bytes.
        # Added extra bytes to account for loss.
        reply = self.axis.readbytes(35)

        # Join the bytes together and strip off the empty signs.
        message = ''.join([chr(x) for x in reply]).strip('\x01\r')

        return message
