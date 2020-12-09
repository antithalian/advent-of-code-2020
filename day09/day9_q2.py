# day 9 question 2

# get input
lines = []
with open('input.txt', 'r') as file:
    for line in file:
        lines.append(int(line))

def valid(preamble, current):

    # brute force...
    for ind, num1 in enumerate(preamble):
        for num2 in (preamble[0:ind] + preamble[ind:]):
            if (num1 + num2) == current:
                return True

    return False

pst = 0
loc = 25
bad = False
while not bad:

    pre = lines[pst:loc]
    cur = lines[loc]
    bad = not valid(pre, cur)
    pst += 1
    loc += 1

bad_num = lines[loc - 1]

def find(bad, nums):

    for ind in range(len(nums)):

        window = 2
        while (ind + 2) < len(nums) and sum(nums[ind:ind + window]) <= bad:
            window += 1
        
        if window >= 3 and sum(nums[ind:ind + (window - 1)]) == bad:
            return min(nums[ind:ind + (window - 1)]) + max(nums[ind:ind + (window - 1)])

    return -1

print(find(bad_num, lines))