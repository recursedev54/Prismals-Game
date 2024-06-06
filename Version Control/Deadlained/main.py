import sys
import os

# Add the root of the project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from QRate.initialize_J import initialize_J
from Deadlained.camera import Camera
from Deadlained.world import World
from higherentities.player import Player
from higherentities.render import Render
from higherentities.update import Update
from highestentities.collide import Collide
from Deadlained.sunbird_feather import initialize_game
from Deadlained.utils import init_opengl, handle_keyboard  # Use actual functions from utils.py
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
    try:
        initialize_J()  # Initialize J
        initialize_game()  # Initialize game settings
        
        pygame.init()
        display = (800, 600)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        init_opengl(display[0], display[1])  # Initialize OpenGL with display dimensions

        camera = Camera()
        world = World()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                handle_keyboard()  # Handle keyboard events

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            world.update()
            world.draw()
            pygame.display.flip()
            pygame.time.wait(10)

    except ImportError as e:
        print(f"Import error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
