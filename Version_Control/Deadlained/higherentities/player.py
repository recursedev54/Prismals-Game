# player.py
import numpy as np

class Player:
    def __init__(self):
        self.position = np.array([0.0, 0.0, 0.0])
        self.affix_height = 1.0  # Set the affix height for the player

    def move_forward(self):
        self.position[2] -= 0.1

    def move_backward(self):
        self.position[2] += 0.1

    def move_left(self):
        self.position[0] -= 0.1

    def move_right(self):
        self.position[0] += 0.1

    def jump(self):
        self.position[1] += 1.0

    def get_front(self):
        return np.array([0.0, 0.0, -1.0])
