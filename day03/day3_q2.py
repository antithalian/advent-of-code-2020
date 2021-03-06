# day 3 question 1
# how many trees, but with varying slopes

# get input
map = []
with open('input.txt', 'r') as file:
    for line in file:
        map.append(list(line.strip()))

# map is basically a list of strings at this point
# get 0-indexed length of map segment, for repetition (it's 31)
length = len(map[0]) - 1
# get 0-indexed height of map, to tell when at bottom
height = len(map) - 1

# count trees for slope w/ change in x c_x and change in y c_y
def count_trees(c_x, c_y):

    # output counter and state vars
    count = 0
    x = 0
    y = 0

    # only worth until at bottom
    while y < height:
        
        # update current position from slope
        x += c_x
        y += c_y

        # check for tree at current position
        if map[y][x % (length + 1)] == '#':
            count += 1

    return count

# make list of slopes
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
# make output list
together = [count_trees(s[0], s[1]) for s in slopes]

# get product
prod = 1
for n in together:
    prod *= n

print(prod)