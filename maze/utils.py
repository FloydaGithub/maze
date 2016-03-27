class RR():
    """the way and range of choose path"""
    total = 1000
    section = [100, 200]
    __tmp = range(total)
    whole = __tmp[:section[0]]
    outside = __tmp[section[0]:section[1]]
    inside = __tmp[section[1]:total]


class MapType():
    empty = '~'
    path = ' '
    wall = 'O'
    # target = 'X'
    target = '\033[1;31;40mX\033[0m'


class Direction():
    __all__ = ['up', 'down', 'left', 'right']
    up = (0, 1)
    down = (0, -1)
    left = (-1, 0)
    right = (1, 0)


class Tile(object):
    _instance = {}

    def __new__(cls, x, y):
        tile = '{x}-{y}'.format(x=x, y=y)
        if not tile in cls._instance:
            cls._instance[tile] = super(Tile, cls).__new__(cls, x, y)
        return cls._instance[tile]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(x = {}, y = {}) '.format(self.x, self.y)

    def __sub__(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def get_around(self):
        rlist = []
        for key in Direction.__all__:
            dirc = getattr(Direction, key)
            rlist.append(Tile(self.x + dirc[0], self.y + dirc[1]))
        return rlist
