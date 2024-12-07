import re

total = 0
input = open("Day 3\input.txt").read()
hits = re.findall("mul\([0-9]*\,[0-9]*\)", input)

def mul(x,y):
    return x*y

for nums in hits:
    total += eval(nums)

print(total)