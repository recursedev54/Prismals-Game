import pygame
from math import sin, cos, radians

class Player:
    def __init__(self, x, y, z):
        self.position = pygame.math.Vector3(x, y, z)
        self.velocity = pygame.math.Vector3(0, 0, 0)
        self.acceleration = pygame.math.Vector3(0, 0, 0)
        self.on_ground = False
        self.speed = 5.0
        self.jump_strength = 5.0
        self.yaw = 0
        self.pitch = 0

    def handle_input(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.position += self.get_front() * self.speed * delta_time
        if keys[pygame.K_s]:
            self.position -= self.get_front() * self.speed * delta_time
        if keys[pygame.K_a]:
            self.position -= self.get_right() * self.speed * delta_time
        if keys[pygame.K_d]:
            self.position += self.get_right() * self.speed * delta_time
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False

    def apply_gravity(self, delta_time):
        gravity = -9.8
        self.acceleration.y = gravity * delta_time
        self.velocity += self.acceleration * delta_time
        self.position += self.velocity * delta_time

        if self.position.y <= 0:  # Simple ground collision
            self.position.y = 0
            self.velocity.y = 0
            self.on_ground = True

    def update(self, delta_time):
        self.apply_gravity(delta_time)
        self.handle_input(delta_time)

    def handle_mouse(self, xrel, yrel):
        self.yaw += xrel * 0.1
        self.pitch -= yrel * 0.1

        if self.pitch > 89:
            self.pitch = 89
        if self.pitch < -89:
            self.pitch = -89

    def get_front(self):
        yaw_rad = radians(self.yaw)
        pitch_rad = radians(self.pitch)
        front = pygame.math.Vector3(
            cos(yaw_rad) * cos(pitch_rad),
            sin(pitch_rad),
            sin(yaw_rad) * cos(pitch_rad)
        )
        return front.normalize()

    def get_right(self):
        front = self.get_front()
        right = pygame.math.Vector3(0, 1, 0).cross(front)
        return right.normalize()
