from utils import *
import random
import copy

def init_map(width, height):
    global map_width, map_height
    map_width, map_height = width, height

    return [[MapStatus.empty] * width for i in xrange(height)]

def _get_pos(cur_pos, direction):
    global map_width, map_height
    x = cur_pos.x + direction[0]
    if x < 0 or x > map_width : return None
    y = cur_pos.y + direction[1]
    if y < 0 or y > map_height : return None
    return x, y

def _search_path(arr, pos, path):
    rand_list = copy.copy(Direction.__all__)
    random.shuffle(rand_list)
    for key in rand_list:
        new_pos = _get_pos(pos, getattr(Direction, key))
        if new_pos is None : continue
        print new_pos
    return '===='

def generate_path(arr, start_pos, end_pos):
    """
    type arr       : Array map
    type start_pos : Pos start
    type end_pos   : Pos end
    rtype: 
        Array map
        List path
    """
    return _search_path(copy.copy(arr), start_pos, [])

print generate_path(init_map(3,4), Pos(0,0), Pos(2,3))



