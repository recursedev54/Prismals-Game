import pygame
from OpenGL.GL import *
from entities.wedge import Wedge
from entities.wate import Wate
from entities.womp import Womp
from entities.blawg import Blawg
from entities4D.waye import get_cos, get_sin  # Updated import

class Collide:
    def __init__(self, player, objects):
        self.player = player
        self.objects = objects
        self.collision_detected = False
        self.collision_color = (0, 1, 1)  # Initial color: Cyan

    def check_collision(self):
        self.collision_detected = False
        for obj in self.objects:
            if isinstance(obj, (Wedge, Wate, Womp, Blawg)):
                if self.is_colliding(obj):
                    self.collision_detected = True
                    break

    def is_colliding(self, obj):
        px, py, pz = self.player.position
        ox, oy, oz = obj.position

        if isinstance(obj, Womp):
            # Simple collision check for a sphere
            radius = 0.5
            distance = ((px - ox) ** 2 + (py - oy) ** 2 + (pz - oz) ** 2) ** 0.5
            return distance < radius

        elif isinstance(obj, Wedge):
            # Simple collision check for an octahedron
            size = 0.5
            return (ox - size < px < ox + size and
                    oy - size < py < oy + size and
                    oz - size < pz < oz + size)

        elif isinstance(obj, Blawg):
            # Adjusted bounding box collision check for Blawg
            size = 1.0  # Increase the size for Blawg
            return (ox - size < px < ox + size and
                    oy - size < py < oy + size and
                    oz - size < pz < oz + size)

        else:
            # Bounding box collision check for other objects
            size = 0.5
            return (ox - size < px < ox + size and
                    oy - size < py < oy + size and
                    oz - size < pz < oz + size)

    def update(self):
        self.check_collision()
        if self.collision_detected:
            self.player.position -= self.player.velocity  # Prevent moving through objects
            self.flash_warning()

    def flash_warning(self):
        # Alternate colors for warning flash
        self.collision_color = (0, 1, 0) if self.collision_color == (0, 1, 1) else (0, 1, 1)
        glColor3f(*self.collision_color)

    def render_collision_boxes(self):
        glColor3f(1, 1, 1)  # White color for bounding boxes
        glBegin(GL_LINES)
        for obj in self.objects:
            if isinstance(obj, (Wedge, Wate, Womp, Blawg)):
                self.draw_bounding_box(obj)
        glEnd()

    def draw_bounding_box(self, obj):
        x, y, z = obj.position
        size = 0.5

        if isinstance(obj, Womp):
            # Draw bounding sphere for Womp
            self.draw_bounding_sphere(x, y, z, size)
        elif isinstance(obj, Wedge):
            # Draw bounding prism for Wedge
            self.draw_bounding_prism(x, y, z, size)
        elif isinstance(obj, Blawg):
            # Draw larger bounding box for Blawg
            self.draw_bounding_cube(x, y, z, 1.0)
        else:
            # Draw regular bounding box for other objects
            self.draw_bounding_cube(x, y, z, size)

    def draw_bounding_sphere(self, x, y, z, radius):
        # Draw the lines of the bounding sphere
        num_segments = 16
        for i in range(num_segments):
            theta = 2.0 * 3.1415926 * float(i) / float(num_segments)
            next_theta = 2.0 * 3.1415926 * float(i + 1) / float(num_segments)

            glVertex3f(x + radius * get_cos(theta), y, z + radius * get_sin(theta))
            glVertex3f(x + radius * get_cos(next_theta), y, z + radius * get_sin(next_theta))

            glVertex3f(x, y + radius * get_cos(theta), z + radius * get_sin(theta))
            glVertex3f(x, y + radius * get_cos(next_theta), z + radius * get_sin(next_theta))

            glVertex3f(x + radius * get_cos(theta), y + radius * get_sin(theta), z)
            glVertex3f(x + radius * get_cos(next_theta), y + radius * get_sin(next_theta), z)

    def draw_bounding_prism(self, x, y, z, size):
        # Draw the lines of the bounding prism (triangular prism)
        height = size
        half_base = size / 2
        vertices = [
            (x - half_base, y - height, z - half_base), (x + half_base, y - height, z - half_base),
            (x, y - height, z + half_base), (x - half_base, y + height, z - half_base),
            (x + half_base, y + height, z - half_base), (x, y + height, z + half_base)
        ]
        edges = [
            (0, 1), (1, 2), (2, 0),  # Base triangle
            (3, 4), (4, 5), (5, 3),  # Top triangle
            (0, 3), (1, 4), (2, 5)   # Vertical edges
        ]
        for edge in edges:
            glVertex3fv(vertices[edge[0]])
            glVertex3fv(vertices[edge[1]])

    def draw_bounding_cube(self, x, y, z, size):
        # Draw the lines of the bounding box
        vertices = [
            (x - size, y - size, z - size), (x + size, y - size, z - size),
            (x + size, y - size, z + size), (x - size, y - size, z + size),
            (x - size, y + size, z - size), (x + size, y + size, z - size),
            (x + size, y + size, z + size), (x - size, y + size, z + size)
        ]
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
