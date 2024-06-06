from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init_opengl(width, height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LEQUAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def handle_keyboard():
    # This function can be expanded to handle keyboard events
    pass
