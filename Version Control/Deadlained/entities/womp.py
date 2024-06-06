from OpenGL.GL import *
from math import cos, sin, radians

class Womp:
    def __init__(self, x, y, z):
        self.position = (x, y, z)

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        glColor3f(0, 0, 1)  # Blue color for the Womp
        glBegin(GL_POLYGON)
        for i in range(360):
            angle = radians(i)
            glVertex3f(0.5 * cos(angle), 0.5 * sin(angle), 0)
        glEnd()
        glPopMatrix()

    def update(self):
        pass  # Implement update method if needed
