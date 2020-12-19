# day 13 challenge 2
# matching times

# read input
with open('input.txt', mode='r') as file:
    pairs = [(int(id), offset) for offset, id in enumerate(file.read().strip().split()[1].split(',')) if id != 'x']
    # build a set of tuples of bus id and offset from start

# tracking vars
t, step = 0, 1

# iterate pairs
for id, offset in pairs:

    # is bus departing?
    while (t + offset) % id != 0:
        t += step
    # check next bus
    step *= id

print(t)
