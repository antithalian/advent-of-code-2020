# day 11 question 2
# this one is gonna need commenting if I ever want to understand it again

from copy import deepcopy
import time

start = time.time()
# read in the basic data
# add a leading and trailing zero to remove the need to check for edge later
seat_map = []
with open('input.txt', mode='r') as file:
    for line in file:
        seat_map.append(['0'] + [char for char in line.strip()] + ['0'])

# add edges to make the check adj logic simpler
seat_map.insert(0, (list('0' * len(seat_map[1]))))
seat_map.append(list('0' * len(seat_map[1])))

# now for q2 we're checking the FIRST seat in any direction
# so ignore floor and check all diagonals

# given a starting row and column along with a direction (specified by c_r and c_c)
# proceed in that direction until we've got something that isn't floor
# then return that
def check_vis(row, col, c_r, c_c, map):

    while map[row][col] == '.':
        row, col = row + c_r, col + c_c

    return map[row][col]

# take the entire map and perform an iteration on it
# operates on the map it's handed but puts all changed into a deep copied map
# this prevents changes from the updated map from interfering with the rules
def iter_map(map):

    # create the new map to update and keep track of whether we've changed anything
    new_map = deepcopy(map)
    changed = False

    # check every non-edge position on the map
    for row in range(1, len(map) - 1):
        for col in range(1, len(map[0]) - 1):

            # check what's visible in every direction
            # c_r and c_c specify the direction to go row-wise and column-wise
            # if they're both zero, we'd be checking the current position
            # don't want that, so ignore it
            visible = [check_vis(row + c_r, col + c_c, c_r, c_c, map)
                        for c_r in range(-1, 2)
                        for c_c in range(-1, 2)
                        if (c_r, c_c) != (0, 0)]

            # count occupied seats by summing the number of '#' in visible
            ct_occ = sum([1 for seat in visible if seat == '#'])

            # apply the rules
            if map[row][col] == 'L' and ct_occ == 0:
                new_map[row][col] = '#'
            if map[row][col] == '#' and ct_occ >= 5:
                new_map[row][col] = 'L'

            # update the change tracking variable if we've changed anything
            if map[row][col] != new_map[row][col] and changed == False:
                changed = True

    # return the updated map and whether anything has changed
    return new_map, changed

# iterate the map until nothing changes
changed = True
while changed:
    curr_map, changed = iter_map(seat_map)
    seat_map = deepcopy(curr_map)

# find the final number of occupied seats by summing all '#' locs
print(sum(line.count('#') for line in seat_map), time.time() - start)