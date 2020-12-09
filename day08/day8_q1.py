# day 8 question 1
# determine when an instruction will be executed twice

# put everything into an array, maintain a dict/hashmap of what's been executed?

# process input
instructions = []
with open('input.txt', 'r') as file:

    for line in file:
        line = line.strip().split(' ')
        instr = (line[0], int(line[1]))
        instructions.append(instr)

visited = {}
ptr = 0
acc = 0
found = False
while not found:

    curr = instructions[ptr]
    if str(ptr) in visited.keys():
        found = True
    else:
        visited[str(ptr)] = 1
        if curr[0] == 'nop':
            ptr += 1
        elif curr[0] == 'acc':
            acc += curr[1]
            ptr += 1
        else:
            ptr += curr[1]

print(acc)