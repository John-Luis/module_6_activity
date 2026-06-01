

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.speed = speed
        self.radius = float(radius)
        self.color = color
        self.on = bool(on)