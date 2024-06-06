from LVX.Godforms.isis import Isis
from LVX.Godforms.apophis import Apophis
from LVX.Godforms.typhon import Typhon
from LVX.quarn import Quarn

class LVX:
    def __init__(self):
        self.isis = Isis()
        self.apophis = Apophis()
        self.typhon = Typhon()
        self.quarn = Quarn()

    def generate_blawg(self, x, y, z):
        blawg = self.isis.create_blawg(x, y, z)
        quarn = self.quarn.add_collider(blawg)
        return quarn

    def generate_wedge(self, x, y, z):
        wedge = self.apophis.create_wedge(x, y, z)
        quarn = self.quarn.add_collider(wedge)
        return quarn

    def generate_womp(self, x, y, z):
        womp = self.typhon.create_womp(x, y, z)
        quarn = self.quarn.add_collider(womp)
        return quarn
