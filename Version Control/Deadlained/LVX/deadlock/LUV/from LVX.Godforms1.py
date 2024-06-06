from LVX.Godforms.apophis import Apophis

class Precis:
    def __init__(self):
        self.apophis = Apophis()

    def create_wedge(self, x, y, z):
        return self.apophis.create_wedge(x, y, z)
