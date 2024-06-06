import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from camera import Camera
from world import World
from higherentities.player import Player
from utils import init_opengl

# Initialize Pygame
pygame.init()

# Constants
FPS = 48

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN)
pygame.display.set_caption("4D Hydrogel Game")
clock = pygame.time.Clock()

# Initialize OpenGL
init_opengl(screen.get_width(), screen.get_height())

# Initialize player, camera, and world
player = Player(x=5, y=5, z=10)
camera = Camera(player=player)
world = World(width=10, height=10)

# Hide mouse cursor and capture it
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# Game loop
running = True
while running:
    delta_time = clock.tick(FPS) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            player.handle_mouse(event.rel[0], event.rel[1])
        else:
            player.handle_event(event)
    
    # Update player
    player.update(delta_time)
    world.update()

    # Render
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    front = player.get_front()
    gluLookAt(
        player.position.x, player.position.y, player.position.z,
        player.position.x + front.x, player.position.y + front.y, player.position.z + front.z,
        0, 1, 0
    )

    world.draw()

    # Display update
    pygame.display.flip()

pygame.quit()
sys.exit()
