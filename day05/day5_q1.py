# day 5 question 1
# boarding passes

# get input
raw = []
with open('input.txt', 'r') as file:
    for line in file:

        # strip line
        line = line.strip()

        # make a tuple of the front and back halves
        dat = (line[0:7], line[7:])

        # append that
        raw.append(dat)

# maxes for rows and columns
row_max = 127
col_max = 7

# find row
def get_row(chars, max):
    
    front = 0
    back = max
    for char in chars:

        if char == 'B':
            front = front + ((back - front) // 2) + 1
        else: # char == 'F'
            back = front + ((back - front) // 2)

    return back # both will be same by this point

# find column
def get_col(chars, max):
    
    left = 0
    right = max
    for char in chars:

        if char == 'R':
            left = left + ((right - left) // 2) + 1
        else: # char == 'L'
            right = left + ((right - left) // 2)

    return right # both same by now

# final array
bpasses = []
# iterate through raw data
for dat in raw:

    # calculate row, col, and seat id
    row = get_row(dat[0], row_max)
    col = get_col(dat[1], col_max)
    sid = (row * 8) + col

    # append it all to bpasses
    bpasses.append((row, col, sid))

max = 0
for p in bpasses:
    if p[2] > max:
        max = p[2]
print(max) # yay 998