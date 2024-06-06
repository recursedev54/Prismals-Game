from LVX.Godforms.isis import Isis
from Deadlock.Deadlane.Shem_HaMephorash.Shem_HaMephorash import ShemHaMephorash
from Deadlock.GodHeadVoices.characters.tsu.summit import Summit
from Deadlock.GodHeadVoices.characters.c.chaga import Chaga

CARDINALTRON_CONSTANT = "#080008"  # Dark color
CARDINALTRON_SECONDARY_CONSTANT = "#216216"  # Light color

class Cardinaltron:
    def __init__(self):
        self.isis = None
        self.color = CARDINALTRON_CONSTANT
        self.secondary_color = CARDINALTRON_SECONDARY_CONSTANT
        self.summit = Summit(self)
        self.chaga = Chaga(self)

    def create_blawg(self, x, y, z):
        if not self.isis:
            self.color = CARDINALTRON_SECONDARY_CONSTANT  # Set to secondary color if unresolved
            self.isis = Isis()  # Create a new Isis instance if unresolved
        else:
            if self.summit.primary_color == self.chaga.primary_color or self.summit.secondary_color == self.chaga.secondary_color:
                resolver = ShemHaMephorash(self, self.isis)
                resolver.resolve_conflict()
                if resolver.godform is None:
                    self.isis = None
        return self.isis.create_blawg(x, y, z) if self.isis else None
