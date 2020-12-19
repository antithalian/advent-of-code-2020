# day 16 challenge 2
# actually figure things out

# can ignore everything prior to line 26 (25 when 0 indexed) when getting nearby
raw = []
with open('input.txt', mode='r') as file:
    for line in file.readlines()[25:]:
        raw.append([int(num) for num in line.strip().split(',')])

# grab our own ticket, too
with open('input.txt', mode='r') as file:
    mine = [int(num) for num in file.readlines()[22].strip().split(',')]

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
# first, remove all invalid tickets
nearby = []
for ticket in raw:

    bad = False
    for num in ticket:
        if num not in valids:
            bad = True
    
    if not bad:
        nearby.append(ticket)

# now we have all GOOD tickets
# up above is a mess so just gonna remake the fields... oops.
fields = {}
with open('input.txt', mode='r') as file:
    lines = file.readlines()[0:20]

    for line in lines:

        field, ranges = line.strip().split(': ')
        ovr_range = set()
        ranges = ranges.split(' or ')
        for r in ranges:
            r = r.split('-')
            for n in range(int(r[0]), int(r[1])):
                ovr_range.add(n)

        fields[field] = ovr_range

field_col = {}
for field, rang in fields.items():

    for ind in range(len(nearby[0])):

        col = set(nearby[n][ind] for n in range(len(nearby)))

        if col.issubset(rang):
            if field in field_col:
                field_col[field].append(ind)
            else:
                field_col[field] = [ind]

# well this is just a giant bork at this point. got the right answer at one point but didn't properly save the commit.
# I need to sleep, so going to leave off here. IDK if I'll come back to fix things and rewrite, catching up needs to be done on other days.