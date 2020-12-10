from collections import deque
from itertools import islice, chain, combinations

inputList = []

with open('day9/day9input.txt', 'r') as f:
    for line in f:
        inputList.append(line[:-1])


def contains_pair_totaling(numbers, total):
    j = 0
    true_or_false = True

    for number1 in islice(numbers, 0, 24):
        j += 1
        for number2 in islice(numbers, j, 25):
            # print(int(number1), int(number2), int(number1) + int(number2))
            if int(number1) + int(number2) == int(total):
                true_or_false = False
    return true_or_false


def exercise2(options, countsTo):
    j = 0
    findThem = []
    for k in options[:-2]:
        summation = int(k)
        findThem.append(int(k))
        j += 1
        for i in options[j:-2]:
            summation += int(i)
            findThem.append(int(i))
            if summation > countsTo:
                findThem.clear()
                break
            elif summation == countsTo:
                print('exercise 2: min =', min(findThem), 'max =', max(findThem), 'sum =', min(findThem) + max(findThem))
                return


if __name__ == '__main__':
    preamble = deque(inputList[0:25])
    i = 24
    for number3 in inputList[26:]:
        i += 1
        boolean = contains_pair_totaling(preamble, inputList[i])
        if boolean:
            print("exercise 1: ", inputList[i])
            break
        preamble.rotate(-1)
        preamble[24] = inputList[i]
    exercise2(inputList, int(inputList[i]))
