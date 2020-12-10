from collections import deque
from itertools import islice, chain, combinations

inputList = []

with open('day10/day10input.txt', 'r') as f:
    for line in f:
        inputList.append(line)
inputList = [int(i) for i in inputList]


def exercise1():
    lastVal = 0
    steps = []

    sortedList = sorted(inputList)
    for i in sortedList:
        difference = i - lastVal
        steps.append(difference)
        lastVal = i
    steps.append(3)
    print("exercise 1 :", steps.count(1)*steps.count(3), "consisting of", steps.count(1), "ones x", steps.count(3),
          "times three")
    return


if __name__ == '__main__':
    exercise1()
    # exercise2()
