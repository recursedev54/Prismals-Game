import sys
import os

# Add the root of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from QRate.init_time import initialize_time
from Deadlained.camera import Camera
from Deadlained.world import World
from higherentities.player import Player
from higherentities.render import Render
from higherentities.update import Update
from highestentities.collide import Collide
from Deadlained.sunbird_feather import initialize_game
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
    initialize_time()  # Initialize time
    initialize_game()  # Initialize game settings
    
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)

    camera = Camera()
    world = World()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        world.update()
        world.draw()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
