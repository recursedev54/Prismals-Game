from LVX.Godforms.typhon import Typhon
from GodHeads.zeus import Zeus
from GodHeads.precis import Precis
from GodHeads.cardinaltron import Cardinaltron

SUN_CONSTANT = "#00FFFF"  # Cyan color

class Sun:
    def __init__(self):
        self.zeus = Zeus()
        self.precis = Precis()
        self.cardinaltron = Cardinaltron()
        self.typhon = Typhon()
        self.color = SUN_CONSTANT

    def resolve(self):
        if not self.zeus.typhon:
            self.zeus.color = "#FFFF00"  # Yellow color if nothing to resolve
        self.zeus.typhon = self.typhon
        self.precis.apophis = self.typhon
        self.cardinaltron.isis = self.typhon
        return True
