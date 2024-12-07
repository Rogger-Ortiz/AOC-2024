input = open("Day 4\input.txt", "r")
lines = []
for line in input:
    lines.append(line.strip("\n"))

def cont(lines, i, j, a, b, letter):
    if letter == "M":
        try:
            if lines[i+a][j+b] == "A":
                if (i+a < 0) or (j+b < 0):
                    return 0
                print(f"Found A at [{i+a}, {j+b}]!")
                return cont(lines, i+a, j+b, a, b, "A")
        except IndexError:
            return 0

    if letter == "A":
        try:
            if lines[i+a][j+b] == "S":
                if (i+a < 0) or (j+b < 0):
                    return 0
                print(f"Found XMAS at [{i+a},{j+b}]!")
                return 1
        except IndexError:
            return 0
    return 0

def findXMAS(lines, i, j):
    print(f"Found X at [{i}, {j}]")
    totalHits = 0
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            try:
                if lines[i+a][j+b] == "M":
                    if (i+a < 0) or (j+b < 0):
                        continue
                    print(f"Found M at [{i+a}, {j+b}] ({lines[i+a][j+b]})!")
                    totalHits += cont(lines, i+a, j+b, a, b, "M")
            except IndexError:
                continue
    print("Exhausted")
    return totalHits

hits = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "X":
            hits.append([i,j])

total = 0
for hit in hits:
    total += findXMAS(lines, hit[0], hit[1])
print(total)
