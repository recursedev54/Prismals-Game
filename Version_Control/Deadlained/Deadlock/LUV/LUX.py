class LUX:
    def __init__(self, hex1, hex2):
        self.hex1 = hex1
        self.hex2 = hex2

    def validate(self):
        # Check if both hex values contain 'f' or 'F'
        return 'f' in self.hex1.lower() and 'f' in self.hex2.lower()
