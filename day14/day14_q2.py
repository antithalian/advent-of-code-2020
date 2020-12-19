# day 14 challenge 2
# bitmasks, but more complicated

# I really need to learn itertools properly
# knowing to use this could've saved me so much time
from itertools import product

# read input
prog = []
with open('input.txt', mode='r') as file:

    for line in file:
        line = line.strip()

        if line[0:4] == 'mask':
            prog.append(['MASK', line.lstrip('mask =')])

        else:
            halves = line.split(' = ')
            h1 = int(halves[0].strip('me[]'))
            h2 = int(halves[1])
            prog.append(['WRIT', h1, h2])

# now have a list of lists
# mask items are formatted as ['MASK', mask bits]
# mem writes are formatted as ['WRIT', addr, val]

# update mask_bits to handle new rules
# we'll now return a list of bits with all permutations
def mask_bits(mask, value):

    # get binary of value and left pad it to 36 bits (mask is assumed 36 bits)
    value = bin(value)[2:]
    value = ((36 - len(value)) * '0') + value

    # create a list of pairs of bits
    pairs = list(zip([bit for bit in mask], [bit for bit in value]))

    # compute the base of masked output
    # don't handle floats yet except to propogate the X
    base_out = ''
    for pair in pairs:

        # if no mask value, skip
        if pair[0] == 'X':
            base_out += 'X'
        # if mask is 0, no change
        elif pair[0] == '0':
            base_out += pair[1]
        else: # if mask is 1, overwrite w/ 1
            base_out += '1'
        
    # now handle creating floating permuation
    outs = []
    # find all indices containing an X
    x_indices = [ind for ind, x in enumerate(base_out) if x == 'X']
    # create combinations for every combination of 1/0 for that number of bits
    combos = product(range(2), repeat=len(x_indices))

    # map those combos onto the original
    for combo in combos:
        
        # create copy of base_out to write this combo into
        new_out = base_out
        # for index in combo and index of x in base_out
        for c_ind, x_ind in enumerate(x_indices):
            # build a new string with the 0/1 for that pos in this combo
            new_out = new_out[0:x_ind] + str(combo[c_ind]) + new_out[x_ind + 1:]
        # write it out to outs
        outs.append(int(new_out, 2))

    return outs

# now need to run actual program

pc = 0
mem = {}
curr_mask = ''
while pc < len(prog):

    if prog[pc][0] == 'MASK':
        curr_mask = prog[pc][1]
    else:
        addrs = mask_bits(curr_mask, prog[pc][1])

        for addr in addrs:
            mem[addr] = prog[pc][2]
    
    pc += 1

print(sum([mem[key] for key in mem.keys()]))