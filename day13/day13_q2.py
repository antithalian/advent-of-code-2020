# day 13 challenge 2
# shuttle contest

# get input
tstamp, step = 0, 1
ids = []
with open('input.txt', mode='r') as file:
    tstamp = int(file.readline())
    for id in file.readline().strip().split(','):
        if id != 'x':
            ids.append(int(id))

