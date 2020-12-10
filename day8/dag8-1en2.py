import copy
inputList = []

with open('day8/day8input.txt', 'r') as f:
    for line in f:
        inputList.append(line.split())


def InstructionFollower(theList):
    iList = []
    acc = 0
    i = 0
    while i not in iList and i < len(theList):
        if theList[i][0] == 'nop':
            iList.append(i)
            i += 1
        elif theList[i][0] == 'acc':
            iList.append(i)
            acc += int(theList[i][1])
            i += 1
        elif theList[i][0] == 'jmp':
            iList.append(i)
            i += int(theList[i][1])
    return acc, i


if __name__ == '__main__':
    tempInputList = []
    acc, poep = InstructionFollower(inputList)
    print("exercise 1: ", acc)

    for change in range(len(inputList)):
        tempInputList = copy.deepcopy(inputList)
        if tempInputList[change][0] == 'nop':
            tempInputList[change][0] = 'jmp'
        elif tempInputList[change][0] == 'jmp':
            tempInputList[change][0] = 'nop'
        acc, poep = InstructionFollower(tempInputList)
        if poep >= len(inputList):
            tempInputList.append(['1', '2'])
            print("exercise 2: ", acc)
