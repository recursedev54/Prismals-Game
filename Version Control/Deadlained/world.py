from OpenGL.GL import *
from LVX.LVX import LVX  # Import LVX

class World:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(height)] for _ in range(width)]
        self.objects = []
        self.lvx = LVX()

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] is not None:
                    self.grid[x][y].draw()
        for obj in self.objects:
            obj.draw()

    def update(self):
        for obj in self.objects:
            obj.update()

    def render_world(self):
        for obj in self.objects:
            obj.draw()
            self.lvx.quarn.draw(obj)
