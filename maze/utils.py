class MapStatus():
    # empty = 0
    # path = 1
    empty = '.'
    path = 'o'


class Pos(object):
    _instance = {}
    def __new__(cls, x, y):
        pos = '{x}-{y}'.format(x = x, y = y)
        if not pos in cls._instance:
            cls._instance[pos] = super(Pos, cls).__new__(cls, x, y)
        return cls._instance[pos]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(x = {}, y = {}) '.format(self.x, self.y)

    def __sub__(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


class Direction():
    __all__ = ['up', 'down', 'left', 'right']
    up = (0, 1)
    down = (0, -1)
    left = (-1, 0)
    right = (1, 0)
