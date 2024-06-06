from LVX.Godforms.isis import Isis

class Cardinaltron:
    def __init__(self):
        self.isis = Isis()

    def create_blawg(self, x, y, z):
        return self.isis.create_blawg(x, y, z)
