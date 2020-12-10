# day 10 challenge 1

# read input
ratings = []
with open('input.txt', 'r') as file:
    for line in file:
        ratings.append(int(line))

ratings.sort()
ratings.append(ratings[-1] + 3)
ratings.insert(0, 0)

one_ct = 0
thr_ct = 0

for ind, jlt in enumerate(ratings):

    if ind < (len(ratings) - 1):
        if (ratings[ind + 1] - jlt) == 1:
            one_ct += 1
        if (ratings[ind + 1] - jlt) == 3:
            thr_ct += 1

print(one_ct * thr_ct)