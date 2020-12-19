# day 15 challenge 2
# memory game but bigger?

# read input
with open('input.txt', mode='r') as file:
    start = [int(num) for num in file.read().strip().split(',')]

# go until 30_000_000 number
go_to = 30_000_000

# hold onto the turn when every number was last spoken
# format is: number is key to a list with the turn it was spoken on
# and whether it was new that time
nums = {num : [turn, turn, True] for turn, num in enumerate(start, start=1)}
last = start[-1]

# print(nums)
# [print(x) for x in start]

for turn in range(len(start) + 1, go_to + 1):

    # print('turn: ', turn)
    
    # if the last number was new, spoken num is 0
    if nums[last][2]:
        spoken = 0
    # if not new, spoken num is current turn - last turn spoken
    else:
        spoken = nums[last][0] - nums[last][1]

    # print('spoke: ', spoken)

    # add spoken number to nums or update it, depending
    if spoken in nums.keys():
        # print("found {} in keys".format(spoken))
        nums[spoken] = [turn, nums[spoken][0], False]
    else:
        # print("added {} to nums".format(spoken))
        nums[spoken] = [turn, turn, True]

    last = spoken

# much brute force, many wow
# still runs in under a minute I think which isn't the worst thing ever

print(last)