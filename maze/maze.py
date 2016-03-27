from utils import *
import random


class Map():
    def __init__(self, start_tile, end_tile, width=32, height=32):
        self.start_tile = Tile(start_tile[0], start_tile[1])
        self.end_tile = Tile(end_tile[0], end_tile[1])
        self.width = width
        self.height = height
        self.arr = [[MapType.empty] * height for i in xrange(width)]
        self.dig_total = 0

    def show_map(self):
        em_total = 0
        wa_total = 0
        print '_' * (self.width + 2)
        for y in xrange(self.height):
            y = self.height - y - 1
            s = '|'
            for x in xrange(self.width):
                if self.arr[x][y] is MapType.empty: em_total += 1
                if self.arr[x][y] is MapType.wall: wa_total += 1

                s += self.arr[x][y]
            print s + '|'
        print '-' * (self.width + 2)
        print 'Path:', self.dig_total
        print 'Empty:', em_total
        print 'Wall:', wa_total

    def inside(self, tile, y=None):
        if y is not None: tile = Tile(tile, y)
        x = tile.x
        y = tile.y
        if x < 0 or x >= self.width: return False
        if y < 0 or y >= self.height: return False
        return True

    def dig_path(self, path, mtype=MapType.path):
        for tile in path:
            self.dig_tile(tile, mtype=mtype)

    def dig_tile(self, tile, mtype=MapType.path):
        if self.arr[tile.x][tile.y] != MapType.path:
            self.dig_total += 1
        self.arr[tile.x][tile.y] = mtype
        # set wall
        for t in tile.get_around():
            x, y = t.x, t.y
            if self.inside(x, y):
                if self.arr[x][y] is MapType.empty:
                    self.arr[t.x][t.y] = MapType.wall

    def search_path(self, tile, target_tile, path, deep, max_deep):
        if deep >= max_deep:
            return None
        if tile == target_tile:
            return path

        tile_list = tile.get_around()
        random.shuffle(tile_list)

        for tile in tile_list:
            if self.inside(tile) is False: continue
            if tile in path: continue

            path.append(tile)
            return self.search_path(tile, target_tile, path, deep + 1,
                                    max_deep)

        return None

    def create_path(self):
        start_tile = self.start_tile
        end_tile = self.end_tile

        while start_tile != end_tile:
            r = random.randrange(RR.total)
            if r in RR.whole:
                range_width = range(self.width)
                range_height = range(self.height)
            elif r in RR.outside:
                range_width = range(min(start_tile.x, end_tile.x))
                range_width.extend(range(
                    max(start_tile.x, end_tile.x), self.width))
                range_height = range(min(start_tile.y, end_tile.y))
                range_height.extend(range(
                    max(start_tile.y, end_tile.y), self.height))
            # elif r in RR.inside:
            else:
                range_width = range(
                    min(start_tile.x, end_tile.x), max(start_tile.x,
                                                       end_tile.x))
                range_height = range(
                    min(start_tile.y, end_tile.y), max(start_tile.y,
                                                       end_tile.y))

            if len(range_width) is 0: range_width = [end_tile.x]
            if len(range_height) is 0: range_height = [end_tile.y]

            tile_a = Tile(
                random.choice(range_width), random.choice(range_height))
            tile_b = Tile(
                random.choice(range_width), random.choice(range_height))

            if start_tile - tile_a <= start_tile - tile_b:
                tile_a, tile_b = tile_b, tile_a
            if end_tile - tile_b <= end_tile - tile_a:
                tile_a, tile_b = tile_b, tile_a

            path = self.search_path(start_tile, tile_a, [], 0,
                                    (start_tile - tile_a) * 2)
            if path is not None:
                self.dig_path(path)
                start_tile = tile_a

            path = self.search_path(end_tile, tile_b, [], 0,
                                    (end_tile - tile_b) * 2)
            if path is not None:
                self.dig_path(path)
                end_tile = tile_b

        self.dig_tile(self.start_tile, mtype=MapType.target)
        self.dig_tile(self.end_tile, mtype=MapType.target)

    def auto_create_path(self, total):
        while self.dig_total < total:
            self.create_path()


if __name__ == '__main__':
    import os, time
    for x in xrange(10):
        os.system('clear')
        print x
        width = 40
        height = 20
        m = Map(
            (random.randrange(width), 0),
            (random.randrange(width), height - 1),
            width=width,
            height=height)
        # m.create_path()
        # m.create_path()
        m.auto_create_path(100)
        m.show_map()
        time.sleep(2.1)
