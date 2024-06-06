class Update:
    def __init__(self, world, delta_time):
        self.world = world
        self.delta_time = delta_time

    def update_world(self):
        self.world.update(self.delta_time)
