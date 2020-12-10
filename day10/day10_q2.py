# day 10 challenge 2

# read input
ratings = []
with open('input.txt', 'r') as file:
    for line in file:
        ratings.append(int(line))

# sort + append port and phone values
ratings.sort()
ratings.append(ratings[-1] + 3)
ratings.insert(0, 0)

from functools import lru_cache
@lru_cache
def ways(index):

    if index >= len(ratings):
        return 1

    cur = ratings[index]
    res = ways(index + 1)

    if ((index + 2) < len(ratings)) and ((ratings[index + 2] - cur) <= 3):

        res += ways(index + 2)

        if ((index + 3) < len(ratings)) and ((ratings[index + 3] - cur) <= 3):

            res += ways(index + 3)

    return res

print(ways(0))