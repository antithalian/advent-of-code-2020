# day 7 question 1
# how many base bag colors can eventually hold a shiny gold bag?

# construct dictionary of what's possible, recursively check???

# get input
rules = {}
with open('input.txt', 'r') as file:

    for line in file:

        line = line.strip().strip('.')

        if line.find('contains') > 0:
            line = line.split(' contains ')
        else:
            line = line.split(' contain ')
        
        rule = {}
        for sub in line[1].split(', '):

            if sub != 'no other bags':
                rule[sub[2:].replace(' bags', '').replace(' bag', '')] = int(sub[0])

        rules[line[0].replace(' bags', '').replace(' bag', '')] = rule


bag_seen = set()

# in the name of golf/quickness!
def check(key):
    for typ in rules[key].keys():
        if typ == 'shiny gold':
            bag_seen.add(bag_type)
            break
        check(typ)

for bag_type in rules.keys():
    check(bag_type)

print(len(bag_seen))