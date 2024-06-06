from OpenGL.GL import *
from entities.blawg import Blawg
from entities.wedge import Wedge
from entities.womp import Womp
from entities.plane import Plane
from entities.wate import Wate
from entities.sky_ceiling import SkyCeiling
from entities.blake import Blake
from higherentities.render import Render  # Import the Render class

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
            Plane(1, 0, -1),
            Wate(0, -1, 0),
            SkyCeiling(0, 10, 0),
            Blake(0, 0, 1)
        ]
        self.render = Render()  # Initialize the Render class

    def init_blawgs(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x + y) % 2 == 0:
                    self.grid[x][y] = Blawg(x, 0, y)

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] is not None:
                    self.grid[x][y].draw()

        for obj in self.objects:
            if isinstance(obj, Blake):
                for blawg in self.grid:
                    for b in blawg:
                        if b is not None and self.render.combine_blawg_and_blake(b, obj):
                            self.objects.remove(obj)
                            self.grid[b.position[0]][b.position[2]] = None
                            break
            else:
                obj.draw()

        self.render.render()  # Render the combined CollisionBlawgs

    def update(self):
        for obj in self.objects:
            obj.update()

    def place_blake(self, x, y, z):
        for obj in self.objects:
            if isinstance(obj, Blawg) and obj.position == (x, y, z):
                obj.place_blake()
                return
        self.objects.append(Blake(x, y, z))
