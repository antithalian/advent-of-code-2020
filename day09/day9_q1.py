# day 9 question 1

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

print(lines[loc - 1])