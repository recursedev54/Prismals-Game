class DEX:
    def __init__(self, hex1, hex2):
        self.hex1 = hex1
        self.hex2 = hex2

    def validate(self):
        # Check if both hex values contain any letter from 'a' to 'e'
        return any(char in self.hex1.lower() for char in 'abcde') and any(char in self.hex2.lower() for char in 'abcde')
