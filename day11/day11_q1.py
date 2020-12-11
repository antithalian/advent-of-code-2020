# day 11 question 1

from copy import deepcopy

seat_map = []
with open('input.txt', mode='r') as file:
    for line in file:
        seat_map.append(['0'] + [char for char in line.strip()] + ['0'])

# add edges to make the check adj logic simpler
seat_map.insert(0, (list('0' * len(seat_map[1]))))
seat_map.append(list('0' * len(seat_map[1])))

# rules:
# floor = .
# empty = L
# occup = #
# 
# if a seat is empty and there are no occupied seats adjacent, it becomes occupied
# if a seat is occupied and four or more adjacent seats are occupied, it becomes empty
# otherwise, state doesn't change

# check the adjacent seats - updated to use the method I used in q2
def check_adj(row, col, map):
    
    # check what's in every direction
    # c_r and c_c specify the direction to look row-wise and column-wise
    # if they're both zero, we'd be checking the current position
    # don't want that, so ignore it
    adj_seats = [map[row + c_r][col + c_c]
                        for c_r in range(-1, 2)
                        for c_c in range(-1, 2)
                        if (c_r, c_c) != (0, 0)]

    # count occupied seats by summing the adj_seats list
    return sum([1 for seat in adj_seats if seat == '#'])

def iter_map(map):

    new_map = deepcopy(map)
    changed = False

    for row in range(1, len(map) - 1):
        for col in range(1, len(map[0]) - 1):

            ct_occ = check_adj(row, col, map)

            # apply the rules
            if map[row][col] == 'L' and ct_occ == 0:
                new_map[row][col] = '#'
            if map[row][col] == '#' and ct_occ >= 4:
                new_map[row][col] = 'L'

            # update the change tracking variable if we've changed anything
            if map[row][col] != new_map[row][col] and changed == False:
                changed = True

    return new_map, changed

# iterate the map until nothing changes
changed = True
while changed:
    curr_map, changed = iter_map(seat_map)
    seat_map = deepcopy(curr_map)

# find the final number of occupied seats by summing all '#' locs
print(sum(line.count('#') for line in seat_map))