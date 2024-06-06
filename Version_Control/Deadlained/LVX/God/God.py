from Celestial.Sun.sun import Sun

class God:
    def __init__(self):
        self.sun = Sun()
        self.sun.resolve()

    def create_blawg(self, x, y, z):
        return self.sun.cardinaltron.create_blawg(x, y, z)

    def create_wedge(self, x, y, z):
        return self.sun.precis.create_wedge(x, y, z)

    def create_womp(self, x, y, z):
        return self.sun.zeus.create_womp(x, y, z)
