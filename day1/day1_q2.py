# day one question 2 solution
# find product of three numbers in input.txt list that sum to 2020

# pull everything out of input file
nums = []
with open('input.txt', 'r') as file:
    for line in file:
        nums.append(int(line))

target = 0
product = 0

# yay brute force
for fir in nums:
    for sec in nums:
        for thi in nums:

            if (fir + sec + thi) == 2020:
                product = fir * sec * thi

print(product)