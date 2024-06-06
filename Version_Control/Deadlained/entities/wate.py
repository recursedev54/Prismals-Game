from OpenGL.GL import *

class Wate:
    def __init__(self, x, y, z):
        self.position = (x, y, z)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 0.5, 0)  # Dark green color for the Wate
        glBegin(GL_QUADS)
        # Large square plane
        size = 1000  # Arbitrarily large to simulate infinity
        glVertex3f(-size, 0, -size)
        glVertex3f(size, 0, -size)
        glVertex3f(size, 0, size)
        glVertex3f(-size, 0, size)
        glEnd()
        glPopMatrix()

    def update(self):
        pass  # Implement update method if needed
