import re

total = 0
input = open("Day 3\input.txt").read()
hits = re.findall("mul\([0-9]*\,[0-9]*\)|do\(\)|don\'t\(\)", input)

def mul(x,y):
    return x*y

flag = 1

for nums in hits:
    if nums == "do()":
        flag = 1
        continue
    if nums == "don\'t()":
        flag = 0
        continue
    if flag == 1:
        total += eval(nums)

print(total)