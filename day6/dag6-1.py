count = 0
totalCount = 0
fullLine = ''
temp = []

with open('day6/day6input.txt', 'r') as f:
    for line in f:
        if line == "\n":
            for i in fullLine:
                if i not in temp:
                    count += 1
                    temp.append(i)
            totalCount += count
            temp = []
            fullLine = ''
            count = 0
        else:
            line = line.strip("\n")
            fullLine += line
    print(totalCount)