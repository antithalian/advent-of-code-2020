# day one solution
# find product of two numbers in input.txt list that sum to 2020

# pull everything out of input file
nums = []
with open('day1_i1.txt', 'r') as file:
    for line in file:
        nums.append(int(line))

target = 0
product = 0

# for each number in the input, figure out what it's complement to 2020 would be
for ini in nums:

    target = 2020 - ini

    # then iterate through and check if its complement exists
    for chk in nums:

        # if it does, compute the product
        # semi-hacky since it assumes there'll only be one pair
        if chk == target:
            product = ini * chk

print(product)