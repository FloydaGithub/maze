class MapStatus():
    empty = 0
    path = 1

class Pos():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

class Direction():
    __all__ = ['up', 'down', 'left', 'right']
    up    = (0, 1)
    down  = (0, -1)
    left  = (-1, 0)
    right = (1, 0)
