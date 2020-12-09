# day 8 question 2
# fix the broken bootcode

from copy import deepcopy

# process input
instructions = []
with open('input.txt', 'r') as file:

    for line in file:
        line = line.strip().split(' ')
        instr = [line[0], int(line[1])]
        instructions.append(instr)

def exec(instrs):

    ptr = 0
    acc = 0
    visited = set()

    while ptr not in visited and ptr != len(instrs):

        visited.add(ptr)
        op, vl = instrs[ptr][0], instrs[ptr][1]

        if op == 'nop':
            ptr += 1
        elif op == 'acc':
            acc += vl
            ptr += 1
        else:
            ptr += vl

    return ptr, acc

switch = {'nop' : 'jmp', 'jmp' : 'nop'}
for ind, instr in enumerate(instructions):

    if instr[0] == 'nop' or instr[0] == 'jmp':
        chgd_instrs = deepcopy(instructions)
        chgd_instrs[ind][0] = switch[instr[0]]
        ptr, acc = exec(chgd_instrs)

        if ptr == len(instructions):
            print(acc)
            break
