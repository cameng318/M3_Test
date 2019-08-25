def to_hex(val, byte):
    """ Convert a value to hex format. 0 is appended in the front for the number of bytes. """
    return ('{:0'+str(byte)+'X}').format(val)


class Stage:
    """ List of commands as defined in the M3-LS-1.8-6-Command-and-Control-Reference-Guide. """
    def __init__(self):
        pass

    def send(self, msg):
        pass

    def get(self):
        pass

    def move_to_target(self, tgt):
        """ Move the linear stage to the target position. """
        target = tgt

        # Limit the target to an acceptable range.
        if target > 12000:
            target = 12000
        elif target < 0:
            target = 0

        self.send('<08 ' + to_hex(target, 8) + '>\r')
        return self.get()

    def view_closed_loop_status_and_position(self):
        self.send('<10>\r')
        return self.get().rstrip('\x01\r'')

    def frequency_calibration(self):
        """ Run the automatic frequency calibration. """
        self.send('<87 5>\r')
        return self.get()


# Unused commands
"""
    def read_the_firmware_version(self):
        self.send('<01>\r')
        return self.get()

    def halt_the_motor(self):
        self.send('<03>\r')
        return self.get()

    def select_open_loop_drive_mode(self):
        self.send('<20 0>\r')
        return self.get()

    def select_closed_loop_drive_mode(self):
        self.send('<20 1>\r')
        return self.get()
"""
