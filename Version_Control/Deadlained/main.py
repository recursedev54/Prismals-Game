import os
import sys
import pygame
from pygame.locals import *
from OpenGL.GL import *  # Import everything from OpenGL.GL
from OpenGL.GLUT import *  # Import everything from OpenGL.GLUT
import numpy as np

# Add the Version_Control directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Deadlained.camera import Camera
from Deadlained.world import World
from Deadlained.utils import some_util_function  # Replace with actual utility function if needed

def sunbird():
    # Add sunbird function details here
    pass

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Prismals Game")

    # Initialize the world and camera
    world = World()
    camera = Camera(world.player)

    # OpenGL settings
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update game logic
        world.update()
        
        # Render the scene
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        world.draw()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    sunbird()
    main()
