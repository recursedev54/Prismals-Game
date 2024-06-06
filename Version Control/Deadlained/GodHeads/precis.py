from LVX.Godforms.apophis import Apophis
from Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash import ShemHaMephorash
from Deadlock.GodHeadVoices.characters.tsu.summit import Summit
from Deadlock.GodHeadVoices.characters.c.chaga import Chaga

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
            if self.summit.primary_color == self.chaga.primary_color or self.summit.secondary_color == self.chaga.secondary_color:
                resolver = ShemHaMephorash(self, self.apophis)
                resolver.resolve_conflict()
                if resolver.godform is None:
                    self.apophis = None
        return self.apophis.create_wedge(x, y, z) if self.apophis else None
