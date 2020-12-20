# day 17 q1
# conway cubes...

from copy import deepcopy
from pprint import pprint

# read in initial map
map = []
with open('input.txt', mode='r') as file:
# with open('test_input.txt', mode='r') as file:

    for line in file:
        map.append(['.'] + [char for char in line.strip()] + ['.'])
    map.insert(0, ['.'] * len(map[0]))
    map.append(['.'] * len(map[0]))

# build map into dimension (i.e. 3D)
up = [(['.'] * len(map[0])) for n in range(len(map))]
dimension = [deepcopy(up), map, deepcopy(up)]

# for p in dimension:
#     pprint(p)

# expand boundary of dimension, adding one plane to top and bottom
# and a new line of inactive cells around edges of all current planes
def expand_dimension(dimension):
    
    # add new border to existing layers
    for plane in dimension:

        # first add to the front and back of each line in plane
        for line in plane:
            line.insert(0, '.')
            line.append('.')

        # then add the new top and bottom
        plane.insert(0, ['.'] * len(plane[0]))
        plane.append(['.'] * len(plane[0]))

    # add new top and bottom layers
    dimension.insert(0, [(['.'] * len(dimension[0][0])) for n in range(len(dimension[0]))])
    dimension.append([(['.'] * len(dimension[0][0])) for n in range(len(dimension[0]))])

    return dimension

# check the box around the given coordinates
# returns number of adjacent active locs
def check_neighbors(y, z, x, dimension):

    # check all surroundings
    check_list = [(c_x, c_y, c_z)
                    for c_x in range(-1, 2)
                    for c_y in range(-1, 2)
                    for c_z in range(-1, 2)
                    if (c_x, c_y, c_z) != (0, 0, 0)
                    if c_x + x in range(len(dimension[0][0]))
                    if c_y + y in range(len(dimension))
                    if c_z + z in range(len(dimension[0]))]

    ct_active = 0
    for diff in check_list:

        # print(diff)

        # get actual coords to check based on inputs
        k_x = x + diff[0]
        k_y = y + diff[1]
        k_z = z + diff[2]

        # dimension is mapped as y being vertical axis
        # print(k_y, k_z, k_x, sep=', ')
        # print()
        if dimension[k_y][k_z][k_x] == '#':
            ct_active += 1

    return ct_active

# simulation runner
def step(dimension):

    # prep output as deep copy of dimension - avoid side effects
    output = deepcopy(dimension)

    # iterate through valid locations in dimension
    for y in range(len(dimension)):
        for z in range(len(dimension[0])):
            for x in range(len(dimension[0][0])):

                # get count of active neighbors
                ct_active = check_neighbors(y, z, x, dimension)

                # follow rule for active
                if dimension[y][z][x] == '#' and ct_active not in (2, 3):
                    output[y][z][x] = '.'
                # follow rule for inactive
                elif dimension[y][z][x] == '.' and ct_active == 3:
                    output[y][z][x] = '#'

    return expand_dimension(output)

# run simulation
for c in range(6):
    for p in dimension:
        pprint(p)
        print()
    dimension = step(dimension)

# count active in final
count = 0
for y in range(len(dimension)):
        for z in range(1, len(dimension[0])):
            for x in range(len(dimension[0][0])):
                if dimension[y][z][x] == '#':
                    count += 1

print(count)