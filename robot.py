import math


class Robot:

    def __init__(self):

        self.x = 100
        self.y = 550

        self.speed = 3

        self.state = "IDLE"

        self.collected = 0

    def move_to(self, tx, ty):

        dx = tx - self.x
        dy = ty - self.y

        dist = math.sqrt(dx * dx + dy * dy)

        if dist < self.speed:
            self.x = tx
            self.y = ty
            return True

        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist

        return False