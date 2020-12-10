
with open('day2/day2puzzle1.txt', 'r') as f:
    passwordStringArray = f.readlines()

validPasswordCount = 0

if __name__ == '__main__':
    for line in passwordStringArray:
        infoSplit = line.split()
        numbers = infoSplit[0].split("-")
        letterWithColon = infoSplit[1]
        letter = letterWithColon[0:1]
        wachtwoord = infoSplit[2]
        if (wachtwoord[int(numbers[0])-1] == letter) != (wachtwoord[int(numbers[1])-1] == letter):
            validPasswordCount += 1
    print(validPasswordCount)
