from OpenGL.GL import *

class SkyCeiling:
    def __init__(self, x, y, z, size=1.0):
        self.position = (x, y, z)
        self.size = size

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0.5, 0.5, 1)  # Light blue color for the SkyCeiling
        glBegin(GL_QUADS)
        # Define vertices for a square plane
        glVertex3f(-self.size, 0, -self.size)
        glVertex3f(self.size, 0, -self.size)
        glVertex3f(self.size, 0, self.size)
        glVertex3f(-self.size, 0, self.size)
        glEnd()
        glPopMatrix()

    def update(self):
        pass  # Implement update method if needed
