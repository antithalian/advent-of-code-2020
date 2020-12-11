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

def check_adj(row, col, map):
    
    up_left = map[row - 1][col - 1]
    up = map[row - 1][col]
    up_right = map[row - 1][col + 1]
    left = map[row][col - 1]
    right = map[row][col + 1]
    dn_left = map[row + 1][col - 1]
    dn = map[row + 1][col]
    dn_right = map[row + 1][col + 1]

    adj_seats = [up, dn, up_left, up_right, left, right, dn_left, dn_right]

    ct_e = len([e for e in adj_seats if e == 'L'])
    ct_o = len([o for o in adj_seats if o == '#'])

    # return True if changed, False if not
    if map[row][col] == 'L':
        if ct_o == 0: # aaaand here was the bug - read the spec properly!
            return '#', True
        else:
            return 'L', False
    elif map[row][col] == '#':
        if ct_o >= 4:
            return 'L', True
        else:
            return '#', False
    else:
        return map[row][col], False


def iter_map(map):

    new_map = deepcopy(map)
    changed = False

    for row in range(1, len(map) - 1):
        for col in range(1, len(map[0]) - 1):

            new_map[row][col], iter_change = check_adj(row, col, map)
            if not changed and iter_change == True:
                changed = True

    return new_map, changed

changed = True
while changed:
    curr_map, changed = iter_map(seat_map)
    seat_map = deepcopy(curr_map)

occupied = 0
for row in range(1, len(seat_map) - 1):
    for col in range(1, len(seat_map[0]) - 1):
        if seat_map[row][col] == '#':
            occupied += 1

print(occupied)