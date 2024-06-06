from OpenGL.GL import *
from entities.blawg import Blawg
from entities.wedge import Wedge
from entities.womp import Womp
from entities.plane import Plane
from entities.wate import Wate
from entities.sky_ceiling import SkyCeiling  # Import the SkyCeiling entity

class World:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(height)] for _ in range(width)]
        self.init_blawgs()
        self.objects = [
            Blawg(0, 0, 0),
            Wedge(2, 0, 2),
            Womp(-2, 0, -2),
            Plane(1, 0, -1),  # Add an instance of Plane
            Wate(0, -1, 0),  # Wate is below the Blawg
            SkyCeiling(0, 10, 0)  # Add an instance of SkyCeiling 10 Blawgs above
        ]

    def init_blawgs(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x + y) % 2 == 0:  # Add Blawg at alternate positions for example
                    self.grid[x][y] = Blawg(x, 0, y)

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
