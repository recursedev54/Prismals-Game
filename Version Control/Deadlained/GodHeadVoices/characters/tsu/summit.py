class Summit:
    def __init__(self, godhead):
        self.godhead = godhead

    def resolve(self):
        if hasattr(self.godhead, 'secondary_color'):
            self.godhead.color = self.godhead.secondary_color
        return True
