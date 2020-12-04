# day 4 question 2 solution
# validate passports but with more validation

# extra validation bits took some help from a redditor since I suck at regex :(
# really need to put in some work on learning that

# starting to use fileinput today
# so arg will have to be input.txt
import fileinput
import re # for extra validation

# check height
def height(val):
    if 'cm' in val:
        n, r = val.split('cm', maxsplit=1)
        return r == '' and 150 <= int(n) <= 193
    if 'in' in val:
        n, r = val.split('in', maxsplit=1)
        return r == '' and 59 <= int(n) <= 76
    return False

# check valid
def validate(pair):
    k, v = pair.split(':')

    if k == 'byr':
        return len(v) == 4 and 1920 <= int(v) <= 2002
    if k == 'iyr':
        return len(v) == 4 and 2010 <= int(v) <= 2020
    if k == 'eyr':
        return len(v) == 4 and 2020 <= int(v) <= 2030
    if k == 'hgt':
        return height(v)
    if k == 'hcl':
        return re.fullmatch(r'#[0-9a-f]{6}', v)
    if k == 'ecl':
        return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth',]
    if k == 'pid':
        return re.fullmatch(r'[0-9]{9}', v)
    if k == 'cid':
        return True

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
            if validate(datum):
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