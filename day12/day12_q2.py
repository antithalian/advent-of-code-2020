# day 12 challenge 2

import math

# get input data
instructions = []
with open('input.txt', 'r') as file:
    for line in file:
        instructions.append((line[0], int(line[1:])))

# using rotate function from here: https://stackoverflow.com/questions/34372480/
def rotate(origin, point, angle):
    
    # Rotate a point counterclockwise by a given angle around a given origin.
    # The angle should be given in radians.
    
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    
    # modified to return ints
    return int(round(qx)), int(round(qy))

boat = {'x' : 0, 'y' : 0}
wypt = {'x' : 10, 'y' : 1}
for instruction in instructions:

    op, val = instruction

    # handle NSEW to move waypoint in direction
    if op in 'NSEW':

        if op == 'N':
            wypt['y'] += val
        elif op == 'S':
            wypt['y'] -= val
        elif op == 'E':
            wypt['x'] += val
        else: # == W
            wypt['x'] -= val

    # handle rotating waypoint around boat
    elif op in 'LR':

        # flip values for R to be negative since they go clockwise around the unit circle
        if op == 'R':
            val = -val
            
        wypt['x'], wypt['y'] = rotate((0, 0), (wypt['x'], wypt['y']), math.radians(val))

    # handle going forward to the waypoint
    else: # == 'F'

        # waypoint position is always relative to the ship, so no need to push that way out
        # that or I accidentally got this right
        boat['y'] += wypt['y'] * val
        boat['x'] += wypt['x'] * val


print(abs(boat['x']) + abs(boat['y']))