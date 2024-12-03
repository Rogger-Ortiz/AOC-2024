input = open("Day 2\\input.txt", "r")
total = 0

def problemSolver(nums):
    flag = 0
    delta = []
    for i in range(len(nums)-1):
        delta.append(int(nums[i])-int(nums[i+1]))

    # Check if there is a change outside of limits or if no change at all
    limits = [-3, -2, -1, 1, 2, 3]
    for num in delta:
        if num not in limits:
            flag = 1
            break
    if flag == 1:
        flag = 0
        return 0

    # Check if all deltas are +ve or -ve
    pos = 0
    neg = 0
    for num in delta:
        if num > 0:
            pos += 1
        if num < 0:
            neg += 1
    if pos > 0 and neg > 0:
        return 0

    # Passed checks, add to safe total
    return 1

for line in input:
    nums = line.strip("\n").split(" ")
    result = problemSolver(nums)

    if result == 0:
        for i in range(len(nums)):
            newlist = nums.copy()
            del newlist[i]
            newresult = problemSolver(newlist)
            if newresult == 1:
                result = 1
                break
    
    total += result

print(total)
