from Celestial.Sun.sun import Sun
from LVX.quarn import Quarn

class LVX:
    def __init__(self):
        self.sun = Sun()
        self.sun.resolve()
        self.quarn = Quarn()

    def generate_blawg(self, x, y, z):
        blawg = self.sun.cardinaltron.create_blawg(x, y, z)
        quarn = self.quarn.add_collider(blawg)
        return quarn

    def generate_wedge(self, x, y, z):
        wedge = self.sun.precis.create_wedge(x, y, z)
        quarn = self.quarn.add_collider(wedge)
        return quarn

    def generate_womp(self, x, y, z):
        womp = self.sun.zeus.create_womp(x, y, z)
        quarn = self.quarn.add_collider(womp)
        return quarn
