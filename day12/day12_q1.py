# day 12 challenge 1
from collections import deque

# get input data
instructions = []
with open('input.txt', 'r') as file:
    for line in file:
        instructions.append((line[0], int(line[1:])))

# x and y are 0, facing is 0 = east
curr = {'x' : 0, 'y' : 0, 'f' : deque(['E', 'S', 'W', 'N'])}
for instruction in instructions:

    op, val = instruction

    # handle NSEW just go in direction
    if op in 'NSEW':

        if op == 'N':
            curr['y'] += val
        elif op == 'S':
            curr['y'] -= val
        elif op == 'E':
            curr['x'] += val
        else: # == W
            curr['x'] -= val

    # handle changing boat angle
    elif op in 'LR':

        turns = val // 90
        if op == 'L':
            curr['f'].rotate(turns)
        else: # == R
            curr['f'].rotate(-turns)

    # handle going forward in whatever the current angle is
    else:

        facing = curr['f'][0]

        if facing == 'N':
            curr['y'] += val
        elif facing == 'S':
            curr['y'] -= val
        elif facing == 'E':
            curr['x'] += val
        else: # == W
            curr['x'] -= val

print(abs(curr['x']) + abs(curr['y']))