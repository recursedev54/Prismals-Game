from OpenGL.GL import *

class Wedge:
    def __init__(self, x, y, z):
        self.position = (x, y, z)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 1, 0)  # Green color for the Wedge
        glBegin(GL_TRIANGLES)
        # Define vertices for a triangular shape
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glEnd()
        glPopMatrix()

    def update(self):
        pass  # Implement update method if needed
