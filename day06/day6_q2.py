# day 6 question 2
# more customs declarations

groups = []
group = {}
with open('input.txt', 'r') as file:


    num = 0
    for line in file:
        line = line.strip()
        

        if not line:
            group['num'] = num
            num = 0
            groups.append(group)
            group = {}

        else:
            num += 1
            for char in line:

                if char in group.keys():
                    group[char] += 1
                else:
                    group[char] = 1

def count_same(group):

    q_same = 0
    for key in group.keys():

        if key != 'num' and group[key] == group['num']:
            q_same += 1

    return q_same
    
print(sum([count_same(group) for group in groups]))