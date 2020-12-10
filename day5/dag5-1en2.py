rows = []
columns = []
maxSearch = []
place = -1

with open('day5/day5input.txt', 'r') as f:
    lines = f.readlines()

if __name__ == '__main__':
    for lineText in lines:
        place += 1
        rows.append(lineText[:7])
        rows[place] = int(rows[place].replace('F', '0').replace('B', '1'), 2)
        columns.append(lineText[7:10])
        columns[place] = int(columns[place].replace('L', '0').replace('R', '1'), 2)
        maxSearch.append(rows[place] * 8 + columns[place])

    print(rows)
    print(columns)
    print(max(maxSearch))
    res = [ele for ele in range(max(maxSearch)+1) if ele not in maxSearch]
    print(str(res))
