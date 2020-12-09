# day 7 question 2
# how many bags inside my one shiny gold bag?

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

num = 0
def count(key):

    global num
    num += sum(rules[key].values())
    for bag_type, quant in rules[key].items():
        for _ in range(quant):
            count(bag_type)

count('shiny gold')
print(num)