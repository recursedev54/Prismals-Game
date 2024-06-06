from GodHeads.zeus import Zeus
from GodHeads.precis import Precis
from GodHeads.cardinaltron import Cardinaltron

class God:
    def __init__(self):
        self.zeus = Zeus()
        self.precis = Precis()
        self.cardinaltron = Cardinaltron()

    def resolve_godheads(self):
        # Resolve the relationships and dependencies
        self.zeus.typhon = self.precis.apophis
        self.precis.apophis = self.cardinaltron.isis
        self.cardinaltron.isis = self.zeus.typhon

    def create_blawg(self, x, y, z):
        return self.cardinaltron.create_blawg(x, y, z)

    def create_wedge(self, x, y, z):
        return self.precis.create_wedge(x, y, z)

    def create_womp(self, x, y, z):
        return self.zeus.create_womp(x, y, z)
