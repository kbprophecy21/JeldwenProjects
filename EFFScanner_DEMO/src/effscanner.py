import serial


PORT = '/dev/ttyUSB0'  # Adjust this to your serial port


class EFFScanner:
    # A class to handle the EFF Scanner operations over a serial connection.
    def __init__(self, port=PORT, baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self):
        self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=self.timeout)

    def disconnect(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def scan_barcode(self):
        """
        Reads a line from the serial port and returns it as a string.
        """
        if not self.serial_conn or not self.serial_conn.is_open:
            self.connect()
        line = self.serial_conn.readline().decode('utf-8').strip()
        return line

    def scan_and_update(self, data_manager):
        """
        Scans a barcode and updates the DataManager with the parsed data.
        """
        barcode_data = self.scan_barcode()
        if barcode_data:
            data_manager.update_from_barcode(barcode_data)
            return True
        return False






