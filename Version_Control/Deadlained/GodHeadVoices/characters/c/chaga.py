class Chaga:
    def __init__(self, godhead):
        self.godhead = godhead
        self.primary_color = "#FFFFFF"  # White color
        self.secondary_color = "#FFFF00"  # Yellow color

    def resolve(self):
        if hasattr(self.godhead, 'secondary_color'):
            if self.godhead.color == self.primary_color or self.godhead.color == self.secondary_color:
                self.godhead.color = self.secondary_color
        return True
