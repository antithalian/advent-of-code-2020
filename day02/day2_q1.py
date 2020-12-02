# day 2 question 1
# password database

# should be as simple as counting occurrences

# input processing
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

    char = item[2]
    cur_ct = 0
    # iterate through pw
    for c in item[3]:
        if c == char:
            cur_ct += 1

    # check if in bounds
    if cur_ct >= item[0] and cur_ct <= item[1]:
        tot_ct += 1

print(tot_ct)