from OpenGL.GL import *

class Blawg:
    def __init__(self, x, y, z):
        self.position = (x, y, z)
        self.has_blake = False  # Track if a Blake is placed at this Blawg

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        if self.has_blake:
            glColor3f(0, 0, 1)  # Blue color for CollisionBlawg
        else:
            glColor3f(1, 0, 0)  # Red color for Blawg
        glBegin(GL_QUADS)
        # Front face
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        # Back face
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        # Left face
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        # Right face
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        # Top face
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        # Bottom face
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glEnd()
        glPopMatrix()

    def update(self):
        pass  # Implement update method if needed

    def place_blake(self):
        self.has_blake = True
