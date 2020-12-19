# day 16 challenge 1
# check error rate

# can ignore everything prior to line 26 (25 when 0 indexed) when getting nearby
nearby = []
with open('input.txt', mode='r') as file:
    for line in file.readlines()[25:]:
        nearby.append([int(num) for num in line.strip().split(',')])

# get validity ranges
vld_ranges = []
with open('input.txt', mode='r') as file:
    for line in file.readlines()[0:20]:
        ranges = line.strip().split(': ')[1].split(' or ')

        for r in ranges:
            r = r.split('-')
            vld_ranges.append((int(r[0]), int(r[1])))

valids = set()
for v in vld_ranges:
    for n in range(v[0], v[1]):
        valids.add(n)

# we now have all valid numbers
# just iterate through tickets and add up all the invalid numbers
errors = []
for ticket in nearby:
    for num in ticket:
        if num not in valids:
            errors.append(num)

print(sum(errors))