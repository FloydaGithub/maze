from utils import *
import random
import copy


class Map():
    def __init__(self, start_pos, end_pos, width=25, height=25):
        self.start_pos = Pos(start_pos[0], start_pos[1])
        self.end_pos = Pos(end_pos[0], end_pos[1])
        self.width = width
        self.height = height
        self.arr = [[MapStatus.empty] * width for i in xrange(height)]

        # self.create_path()

    def show_map(self):
        for y in xrange(self.height - 1, -1, -1):
            s = ''
            for x in xrange(self.width):
                s += str(self.arr[x][y])
            print s
        print

    def dig_path(self, path, status=MapStatus.path):
        for pos in path:
            self.dig_pos(pos, status=status)

    def dig_pos(self, pos, status=MapStatus.path):
        self.arr[pos.x][pos.y] = status

    def can_dig_next(self, cur_pos, direction, path):
        x = cur_pos.x + direction[0]
        if x < 0 or x >= self.width: return None
        y = cur_pos.y + direction[1]
        if y < 0 or y >= self.height: return None
        # if self.arr[x][y] != MapStatus.empty: return None
        next_pos = Pos(x, y)
        if next_pos in path: return None
        # for key in Direction.__all__:
        #     direction = getattr(Direction, key)
        #     x = cur_pos.x + direction[0]
        #     y = cur_pos.y + direction[1]
        #     if self.arr[x][y] == MapStatus.path: return None
        return next_pos

    def search_path(self, cur_pos, ended_pos, path, deep, max_deep):
        if deep >= max_deep:
            return None
        if cur_pos == ended_pos:
            self.dig_path(path)
            return path

        dir_list = copy.copy(Direction.__all__)
        random.shuffle(dir_list)

        tmp_path, tmp_deep = None, max_deep

        for key in dir_list:
            next_pos = self.can_dig_next(cur_pos, getattr(Direction, key),
                                         path)
            if next_pos is None: continue

            path = copy.copy(path)
            path.append(next_pos)

            return self.search_path(next_pos, ended_pos, path, deep + 1,
                                    max_deep)
        return None


    def create_path(self):
        start_pos = self.start_pos
        end_pos = self.end_pos
        self.dig_pos(start_pos) 
        self.dig_pos(end_pos) 

        while start_pos != end_pos:
            rand = random.randrange(100) % 5
            if rand == 0:
                range_width = range(self.width)
                range_height = range(self.height)
            elif rand == 1:
                range_width = range(min(start_pos.x, end_pos.x))
                range_width.extend(range(max(start_pos.x, end_pos.x), self.width))
                range_height = range(min(start_pos.y, end_pos.y))
                range_height.extend(range(max(start_pos.y, end_pos.y), self.height))
            else:
                range_width = range(min(start_pos.x, end_pos.x),max(start_pos.x, end_pos.x))
                range_height = range(min(start_pos.y, end_pos.y),max(start_pos.y, end_pos.y))

            if len(range_width) is 0 : range_width = [start_pos.x]
            if len(range_height) is 0 : range_height = [start_pos.y]

            pos_a = Pos(
                random.choice(range_width),
                random.choice(range_height))
            pos_b = Pos(
                random.choice(range_width),
                random.choice(range_height))

            if start_pos - pos_a <= start_pos - pos_b:
                pos_a, pos_b = pos_b, pos_a
            if end_pos - pos_b <= end_pos - pos_a:
                pos_a, pos_b = pos_b, pos_a

            path = self.search_path(start_pos, pos_a, [], 0, (start_pos - pos_a) * 2)
            if path is not None:
                self.dig_path(path)
                start_pos = pos_a

            path = self.search_path(end_pos, pos_b, [], 0, (end_pos - pos_b) * 2)
            if path is not None:
                self.dig_path(path)
                end_pos = pos_b


a = Map((0, 0), (24, 24))
# a = Map((0, 12), (24, 12))
a.create_path()
a.create_path()
a.show_map()
# Map((0, 12), (24, 12))
# Map((random.randrange(16), random.randrange(16)), (random.randrange(16), random.randrange(16)))
