from LVX.Godforms.apophis import Apophis
from Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash import ShemHaMephorash
from Deadlock.GodHeadVoices.characters.tsu.summit import Summit
from Deadlock.GodHeadVoices.characters.c.chaga import Chaga
from Deadlock.LUX.LUX import LUX
from Deadlock.LUX.DUX import DUX
from Deadlock.LUX.DEX import DEX

PRECIS_CONSTANT = "#FF0000"  # Red color
PRECIS_SECONDARY_CONSTANT = "#00FF00"  # Green color

class Precis:
    def __init__(self):
        self.apophis = None
        self.color = PRECIS_CONSTANT
        self.secondary_color = PRECIS_SECONDARY_CONSTANT
        self.summit = Summit(self)
        self.chaga = Chaga(self)

    def create_wedge(self, x, y, z):
        if not self.apophis:
            self.color = PRECIS_SECONDARY_CONSTANT  # Set to secondary color if unresolved
            self.apophis = Apophis()  # Create a new Apophis instance if unresolved
        else:
            lux_validator = LUX(self.summit.primary_color, self.chaga.primary_color)
            dux_validator = DUX(self.summit.primary_color, self.chaga.primary_color)
            dex_validator = DEX(self.summit.primary_color, self.chaga.primary_color)

            if lux_validator.validate() or dux_validator.validate() or dex_validator.validate():
                resolver = ShemHaMephorash(self, self.apophis)
                resolver.resolve_conflict()
                if resolver.godform is None:
                    self.apophis = None
        return self.apophis.create_wedge(x, y, z) if self.apophis else None
