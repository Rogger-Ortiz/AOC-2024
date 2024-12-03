input = open("Day 2\\input.txt", "r")
total = 0
flag = 0
for line in input:
    delta = []
    nums = line.split(" ")
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
        continue

    # Check if all deltas are +ve or -ve
    pos = 0
    neg = 0
    for num in delta:
        if num > 0:
            pos += 1
        if num < 0:
            neg += 1
    if pos > 0 and neg > 0:
        continue

    # Passed checks, add to safe total
    total += 1

print(total)
