# day 13 challenge 1
# shuttle search

# get input
tstamp = 0
ids = []
with open('input.txt', mode='r') as file:
    tstamp = int(file.readline())
    for id in file.readline().strip().split(','):
        if id != 'x':
            ids.append(int(id))

deps = {}
for id in ids:
    departing = (id * (tstamp // id)) + id
    deps[departing] = id

print((min(deps) - tstamp) * deps[min(deps)])