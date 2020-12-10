import itertools
numberArray = []
plek0 = -1
plek1 = -1
with open('day1/day1puzzle1.txt', 'r') as f:
    numberStringArray = f.readlines()
    numberArray = [int(i) for i in numberStringArray]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(numberArray)
    for base in numberArray:
        plek0 += 1
        for number0 in itertools.islice(numberArray, plek0, None):
            plek1 += 1
            for number1 in itertools.islice(numberArray, plek0, None):
                if base + number0 + number1 == 2020:
                    print(base, number0, number1, base*number0*number1)
        plek1 = 0