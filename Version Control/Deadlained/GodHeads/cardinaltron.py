from LVX.Godforms.isis import Isis
from LVX.shatter import shatter

CARDINALTRON_CONSTANT = "#00FFFF"  # Cyan color
CARDINALTRON_UNRESOLVED_CONSTANT = "#FFFF00"  # Yellow color for unresolved

class Cardinaltron:
    def __init__(self):
        self.isis = None
        self.color = CARDINALTRON_CONSTANT

    def create_blawg(self, x, y, z):
        if not self.isis:
            self.color = CARDINALTRON_UNRESOLVED_CONSTANT  # Set to yellow if unresolved
            self.isis = Isis()  # Create a new Isis instance if unresolved
        else:
            shatter(self, self.isis)  # Attempt to resolve conflict by shattering
        return self.isis.create_blawg(x, y, z)
