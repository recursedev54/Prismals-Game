from LVX.Godforms.apophis import Apophis
from LVX.shatter import shatter

PRECIS_CONSTANT = "#00FFFF"  # Cyan color
PRECIS_UNRESOLVED_CONSTANT = "#FFFF00"  # Yellow color for unresolved

class Precis:
    def __init__(self):
        self.apophis = None
        self.color = PRECIS_CONSTANT

    def create_wedge(self, x, y, z):
        if not self.apophis:
            self.color = PRECIS_UNRESOLVED_CONSTANT  # Set to yellow if unresolved
            self.apophis = Apophis()  # Create a new Apophis instance if unresolved
        else:
            shatter(self, self.apophis)  # Attempt to resolve conflict by shattering
        return self.apophis.create_wedge(x, y, z)
