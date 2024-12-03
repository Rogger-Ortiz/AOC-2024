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
    num1 = list1[i]
    simscore = 0
    for j in range(len(list2)):
        num2 = list2[j]
        if num2 == num1:
            simscore+=1
        if num2 > num1:
            break
    total+= (num1*simscore)
print(total)