input = open("Day 1\input.txt", "r")
list1 = []
list2 = []
for line in input:
    nums = line.split(" ")
    list1.append(int(nums[0]))
    list2.append(int(nums[-1]))
list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
print(total)