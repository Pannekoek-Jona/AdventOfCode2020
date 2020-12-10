count = 0
totalCount = 0
persons = 0
fullLine = ''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open('day6/day6input.txt', 'r') as f:
    for line in f:
        if line == "\n":
            for j in alphabet:
                if fullLine.count(j) == persons and persons != 0:
                    count += 1
            totalCount += count
            count = 0
            persons = 0
            fullLine = ''
        else:
            line = line.strip("\n")
            fullLine += line
            persons += 1
    print(totalCount)
