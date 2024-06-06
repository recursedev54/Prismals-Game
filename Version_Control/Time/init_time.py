# Version_Control/Time/init_time.py

class Time:
    def __init__(self):
        self.current_time = 0.0

    def update_time(self, delta):
        self.current_time += delta

    def get_current_time(self):
        return self.current_time

# Create a global instance of Time
global_time = Time()
