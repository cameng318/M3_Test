import time
import spidev


def to_hex(val, byte):
    return ('{:0'+str(byte)+'X}').format(val)


class SPIStage:
    def __init__(self, bus, device):
        self.axis = spidev.SpiDev()
        self.axis.open(bus, device)
        self.axis.max_speed_hz = 400000
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

    def read_the_firmware_version(self):
        self.send('<01>\r')
        return self.get()

    def halt_the_motor(self):
        self.send('<03>\r')
        return self.get()

    def move_the_motor_in_timed_open_loop_steps(self, direction, steps, interval, duration):
        self.send('<04 1>\r')
        return self.get()

    def move_to_target(self, tgt):
        target = tgt
        if target > 12000:
            target = 12000
        elif target < 0:
            target = 0
        self.send('<08 ' + to_hex(target, 8) + '>\r')
        return self.get()

    def set_the_open_loop_mode_speed(self, speed):
        self.send('<09 80>\r')
        return self.get()

    def view_closed_loop_status_and_position(self):
        self.send('<10>\r')
        return self.get()

    def select_open_loop_drive_mode(self):
        self.send('<20 0>\r')
        return self.get()

    def select_closed_loop_drive_mode(self):
        self.send('<20 1>\r')
        return self.get()
