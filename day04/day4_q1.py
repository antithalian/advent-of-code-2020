# day 4 question 1 solution
# passport validation

# starting to use fileinput today
# so arg will have to be input.txt
import fileinput

# process input
passpts = []
passpt = set()
for line in fileinput.input():
    
    # strip line
    line = line.strip()

    # check if line is empty
    if not line:
        # append current set to main list and reset the working set
        passpts.append(passpt)
        passpt = set()
    else:
        data = line.split(' ')
        for datum in data:
            passpt.add(datum.split(':')[0])

    # code was apparently broken because it didn't check last element of file, added a newline to input

# passport is valid if length is 7 w/out cid or 8 w/ cid
def valid(pspt):
    
    pspt = set(pspt)
    pspt.add('cid')
    pspt.remove('cid')
    return len(pspt) == 7

valid_count = 0
for passpt in passpts:
    if valid(passpt):
        valid_count += 1

print(valid_count)