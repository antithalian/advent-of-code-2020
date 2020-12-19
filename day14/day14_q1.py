# day 14 challenge 1
# bitmasks

# bitsets/their python equivalent seem useful?

# read input
prog = []
with open('input.txt', mode='r') as file:

    for line in file:
        line = line.strip()

        if line[0:4] == 'mask':
            prog.append(['MASK', line.lstrip('mask =')])

        else:
            halves = line.split(' = ')
            h1 = halves[0].strip('me[]')
            h2 = int(halves[1])
            prog.append(['WRIT', h1, h2])

# now have a list of lists
# mask items are formatted as ['MASK', mask bits]
# mem writes are formatted as ['WRIT', addr, val]

def mask_bits(mask, value):

    # get binary of value and left pad it to 36 bits (mask is assumed 36 bits)
    value = bin(value)[2:]
    value = ((36 - len(value)) * '0') + value

    # create a list of pairs of bits
    pairs = list(zip([bit for bit in mask], [bit for bit in value]))

    # compute the masked output
    out = ''
    for pair in pairs:

        # if no mask value, skip
        if pair[0] == 'X':
            out += pair[1]
        # otherwise, set the output value to what the mask has
        else:
            out += pair[0]

    return int(out, 2)

# now need to run actual program
# I think the fastest way is to create a dict of mem locs and values
# then sum all values

pc = 0
mem = {}
curr_mask = ''
while pc < len(prog):

    if prog[pc][0] == 'MASK':
        curr_mask = prog[pc][1]
    else:
        mem[prog[pc][1]] = mask_bits(curr_mask, prog[pc][2])
    
    pc += 1

print(sum([mem[key] for key in mem.keys()]))