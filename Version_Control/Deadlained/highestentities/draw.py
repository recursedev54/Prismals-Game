from OpenGL.GL import *
from entities.collision_blawg import CollisionBlawg

class Draw:
    def __init__(self):
        self.collision_blawgs = []

    def add_collision_blawg(self, collision_blawg):
        self.collision_blawgs.append(collision_blawg)

    def draw_collision_blawg(self):
        glColor3f(0, 0, 1)  # Blue color for the mesh
        glBegin(GL_LINES)
        for cb in self.collision_blawgs:
            x, y, z = cb.position
            # Draw mesh for the collision blawg
            glVertex3f(x - 0.5, y - 0.5, z - 0.5)
            glVertex3f(x + 0.5, y - 0.5, z - 0.5)

            glVertex3f(x + 0.5, y - 0.5, z - 0.5)
            glVertex3f(x + 0.5, y + 0.5, z - 0.5)

            glVertex3f(x + 0.5, y + 0.5, z - 0.5)
            glVertex3f(x - 0.5, y + 0.5, z - 0.5)

            glVertex3f(x - 0.5, y + 0.5, z - 0.5)
            glVertex3f(x - 0.5, y - 0.5, z - 0.5)

            glVertex3f(x - 0.5, y - 0.5, z + 0.5)
            glVertex3f(x + 0.5, y - 0.5, z + 0.5)

            glVertex3f(x + 0.5, y - 0.5, z + 0.5)
            glVertex3f(x + 0.5, y + 0.5, z + 0.5)

            glVertex3f(x + 0.5, y + 0.5, z + 0.5)
            glVertex3f(x - 0.5, y + 0.5, z + 0.5)

            glVertex3f(x - 0.5, y + 0.5, z + 0.5)
            glVertex3f(x - 0.5, y - 0.5, z + 0.5)

            glVertex3f(x - 0.5, y - 0.5, z - 0.5)
            glVertex3f(x - 0.5, y - 0.5, z + 0.5)

            glVertex3f(x + 0.5, y - 0.5, z - 0.5)
            glVertex3f(x + 0.5, y - 0.5, z + 0.5)

            glVertex3f(x + 0.5, y + 0.5, z - 0.5)
            glVertex3f(x + 0.5, y + 0.5, z + 0.5)

            glVertex3f(x - 0.5, y + 0.5, z - 0.5)
            glVertex3f(x - 0.5, y + 0.5, z + 0.5)
        glEnd()
