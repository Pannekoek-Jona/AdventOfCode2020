outerColor = []
fitsBag = []
contents = []
iList = []
totalCount = []

with open('day7/day7input.txt', 'r') as f:
    for line in f:
        line = line.strip("\n")
        line = line[:-1]
        line = line.replace("bags", '')
        line = line.replace("bag", '')
        line = ''.join([i for i in line if not i.isdigit()])
        line = line.split('contain', 1)
        line[0] = line[0].strip()
        fitsBag.append(line[0])
        findContents = [y.strip() for y in line[1].split(',')]
        contents.append(findContents)
    print(fitsBag)
    print(contents)

if __name__ == '__main__':
    for i in range(len(fitsBag)):
        if "shiny gold" in contents[i]:
            if fitsBag[i] not in outerColor:
                outerColor.append(fitsBag[i])
                iList.append(i)

    while len(totalCount) != len(outerColor):
        for nextOne in outerColor:
            for i in range(len(fitsBag)):
                if nextOne in contents[i]:
                    if fitsBag[i] not in outerColor:
                        outerColor.append(fitsBag[i])
                        iList.append(i)
        totalCount = totalCount + outerColor
    print(outerColor)
    print(len(outerColor))
