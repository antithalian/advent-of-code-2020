# day 6 question 1
# customs declaration

# process input
# looks like the stuff from day 4 should be useful
groups = []
group = set()
with open('input.txt', 'r') as file:

    for line in file:
        line = line.strip()

        if not line:
            groups.append(len(group))
            group = set()

        else:
            for char in line:
                group.add(char)

print(sum(groups))