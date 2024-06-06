from entities.blawg import Blawg
from entities.blake import Blake
from entities.collision_blawg import CollisionBlawg

class Render:
    def __init__(self):
        self.collision_blawgs = []

    def combine_blawg_and_blake(self, blawg, blake):
        if blawg.position == blake.position:
            self.collision_blawgs.append(CollisionBlawg(*blawg.position))
            return True
        return False

    def render(self):
        for collision_blawg in self.collision_blawgs:
            collision_blawg.draw()
