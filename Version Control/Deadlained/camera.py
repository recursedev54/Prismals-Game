import numpy as np
from higherentities.player import Player

class Camera:
    def __init__(self, player):
        self.player = player

    def get_view_matrix(self):
        position = self.player.position
        front = self.player.get_front()
        
        right = np.cross(front, [0, 1, 0])
        up = np.cross(right, front)
        
        return np.array([
            [right[0], up[0], -front[0], 0],
            [right[1], up[1], -front[1], 0],
            [right[2], up[2], -front[2], 0],
            [-np.dot(right, position), -np.dot(up, position), np.dot(front, position), 1]
        ], dtype=float)
