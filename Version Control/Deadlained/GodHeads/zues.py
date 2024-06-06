from LVX.Godforms.typhon import Typhon
from Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash import ShemHaMephorash
from Deadlock.GodHeadVoices.characters.tsu.summit import Summit
from Deadlock.GodHeadVoices.characters.c.chaga import Chaga
from Deadlock.LUX.LUX import LUX
from Deadlock.LUX.DUX import DUX
from Deadlock.LUX.DEX import DEX

ZEUS_CONSTANT = "#00FFFF"  # Cyan color
ZEUS_UNRESOLVED_CONSTANT = "#FFFF00"  # Yellow color for unresolved

class Zeus:
    def __init__(self):
        self.typhon = None
        self.color = ZEUS_CONSTANT
        self.summit = Summit(self)
        self.chaga = Chaga(self)

    def create_womp(self, x, y, z):
        if not self.typhon:
            self.color = ZEUS_UNRESOLVED_CONSTANT  # Set to yellow if unresolved
            self.typhon = Typhon()  # Create a new Typhon instance if unresolved
        else:
            lux_validator = LUX(self.summit.primary_color, self.chaga.primary_color)
            dux_validator = DUX(self.summit.primary_color, self.chaga.primary_color)
            dex_validator = DEX(self.summit.primary_color, self.chaga.primary_color)

            if lux_validator.validate() or dux_validator.validate() or dex_validator.validate():
                resolver = ShemHaMephorash(self, self.typhon)
                resolver.resolve_conflict()
                if resolver.godform is None:
                    self.typhon = None
        return self.typhon.create_womp(x, y, z) if self.typhon else None
