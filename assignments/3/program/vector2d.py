import math

class Vector2D:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))