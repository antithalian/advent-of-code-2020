# day 17 q1
# conway cubes...

from copy import deepcopy
from pprint import pprint

# read in initial map
map = []
with open('input.txt', mode='r') as file:

    for line in file:
        map.append(['.'] + [char for char in line.strip()] + ['.'])
    map.insert(0, ['.'] * len(map[0]))
    map.append(['.'] * len(map[0]))

# build map into dimension (i.e. 3D)
up = [(['.'] * len(map[0])) for n in range(len(map))]
dimension = [deepcopy(up), map, deepcopy(up)]

