# day 2 question 2
# password db but rules are different

# just check and xor indices?
from operator import xor

# get input (copied from q1)
pw_db = []
with open('input.txt', 'r') as file:
    for line in file:

        # reformat line for splitting
        line = line.replace('-', ';')
        line = line.replace(': ', ';')
        line = line.replace(' ', ';')
        line = line.split(';')

        # append tuple with all attributes
        # format is (min, max, char, pw)
        out = [int(line[0]), int(line[1]), line[2], line[3].rstrip()]
        pw_db.append(tuple(out))

# iterate through whole db
tot_ct = 0
for item in pw_db:

    # grab everything now for clarity
    # subtract 1 from positions since no index zero
    p1 = item[0] - 1
    p2 = item[1] - 1
    char = item[2]
    pw = item[3]

    cur_ct = 0
    # check if correct
    if xor((pw[p1] == char), (pw[p2] == char)):
        tot_ct += 1

print(tot_ct)