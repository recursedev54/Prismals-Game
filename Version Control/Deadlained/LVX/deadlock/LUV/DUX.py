class DUX:
    def __init__(self, hex1, hex2):
        self.hex1 = hex1
        self.hex2 = hex2

    def validate(self):
        # Check if both hex values contain '1' or '0'
        return '1' in self.hex1 and '1' in self.hex2 or '0' in self.hex1 and '0' in self.hex2
