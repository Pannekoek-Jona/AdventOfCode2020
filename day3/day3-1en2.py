with open('day3/day3puzzle1.txt', 'r') as f:
    treeArray = f.readlines()

trees = 0
place = 0
offset = 0
sum = 1
stepSize = [1, 3, 5, 7]

if __name__ == '__main__':
    length = len(treeArray[0]) - 1
    for iteration in stepSize:
        trees = 0
        place = 0
        offset = 0
        print('íteration = ', iteration)
        for line in treeArray[1:]:
            place = place + iteration
            if line[place] == '#':
                trees += 1
            if place > length - 1 - iteration:
                offset = length - place
                place = 0 - offset
        print('number of trees in iteration:', iteration, 'is', trees)
        sum = sum * trees
        print('sum', sum)
    count = 1
    trees = 0
    place = 0
    offset = 0
    for line in treeArray[1:]:
        count += 1
        if count % 2 == 1:
            place = place + 1
            print(line[:place+1])
            print(line[place], place)
            if line[place] == '#':
                trees += 1
            if place > length - 1 - 1:
                offset = length - place
                print('offset', offset)
                place = 0 - offset
    print(trees)
    sum = sum * trees
    print(sum)
