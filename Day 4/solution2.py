input = open("Day 4\input.txt", "r")
lines = []
for line in input:
    lines.append(line.strip("\n"))

hits = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "A":
            hits.append([i,j])

total = 0
for hit in hits:
    x = hit[0]
    y = hit[1]

    valid = 0
    try:
        if lines[x-1][y-1] == "M":
            if lines[x+1][y+1] == "S":
                if (not (x-1 < 0)) and (not (y-1 < 0)):
                    valid += 1
    except IndexError:
        pass

    try:

        if lines[x+1][y+1] == "M":
            if lines[x-1][y-1] == "S":
                if (not (x-1 < 0)) and (not (y-1 < 0)):
                    valid += 1
    except IndexError:
        pass

    try:

        if lines[x-1][y+1] == "S":
            if lines[x+1][y-1] == "M":
                if (not (x-1 < 0)) and (not (y-1 < 0)):
                    valid += 1
    except IndexError:
        pass

    try:

        if lines[x+1][y-1] == "S":
            if lines[x-1][y+1] == "M":
                if (not (x-1 < 0)) and (not (y-1 < 0)):
                    valid += 1
    except IndexError:
        pass

    if valid == 2:
        total+=1

print(total)
