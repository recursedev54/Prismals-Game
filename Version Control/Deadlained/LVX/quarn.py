from OpenGL.GL import *

class Quarn:
    def add_collider(self, entity):
        entity.has_collider = True
        return entity

    def draw(self, entity):
        if hasattr(entity, 'has_collider') and entity.has_collider:
            glPushMatrix()
            glTranslatef(*entity.position)
            glColor3f(1, 1, 0)  # Yellow color for the collider
            glBegin(GL_QUADS)
            size = 0.5
            # Front face
            glVertex3f(-size, -size, size)
            glVertex3f(size, -size, size)
            glVertex3f(size, size, size)
            glVertex3f(-size, size, size)
            # Back face
            glVertex3f(-size, -size, -size)
            glVertex3f(-size, size, -size)
            glVertex3f(size, size, -size)
            glVertex3f(size, -size, -size)
            # Left face
            glVertex3f(-size, -size, -size)
            glVertex3f(-size, -size, size)
            glVertex3f(-size, size, size)
            glVertex3f(-size, size, -size)
            # Right face
            glVertex3f(size, -size, -size)
            glVertex3f(size, size, -size)
            glVertex3f(size, size, size)
            glVertex3f(size, -size, size)
            # Top face
            glVertex3f(-size, size, -size)
            glVertex3f(-size, size, size)
            glVertex3f(size, size, size)
            glVertex3f(size, size, -size)
            # Bottom face
            glVertex3f(-size, -size, -size)
            glVertex3f(size, -size, -size)
            glVertex3f(size, -size, size)
            glVertex3f(-size, -size, size)
            glEnd()
            glPopMatrix()
