import pandas as pd
pd.set_option('display.max_rows', None)

with open('day4/day4input.txt', 'r') as f:
    i = 0
    entries = {}
    dicts = {}
    for line in f:
        if line == "\n":
            entries[i] = dicts
            dicts = {}
            i += 1
        else:
            line = line.strip("\n")
            dicts.update(dict(item.split(':') for item in line.split(" ")))
    entries[i] = dicts          # Vraag mij alsjeblieft niet waarom. Ik snap niet waar een file eindigt. Als ik dit niet doe leest hij een line te weinig, doe ik het wel dan is er een line te veel.
    dicts = {}
    i += 1

if __name__ == '__main__':
    print(entries)
    df = pd.DataFrame.from_dict(entries, orient='index')
    print(df)
    print(len(df.index))
    dfNoNan = df.dropna(axis=0, subset={'iyr', 'ecl', 'hgt', 'pid', 'byr', 'hcl', 'eyr'})
    for index, row in dfNoNan.iterrows():
        number = ''.join([i for i in row['pid'] if i.isdigit()])
        if int(row['byr']) > 2002 or int(row['byr']) < 1920:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue
        elif int(row['iyr']) > 2020 or int(row['iyr']) < 2010:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue
        elif int(row['eyr']) > 2030 or int(row['eyr']) < 2020:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue
        elif row['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue
        elif len(row['hcl']) != 7:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue
        elif len(number) != 9:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue

        incm = ''.join([i for i in row['hgt'] if not i.isdigit()])
        length = int(''.join([i for i in row['hgt'] if i.isdigit()]))
        # print(incm)
        if incm == 'cm':
            if length < 150 or length > 193:
                dfNoNan = dfNoNan.drop(labels=index, axis=0)
                continue
        elif incm == 'in':
            if length < 59 or length > 76:
                dfNoNan = dfNoNan.drop(labels=index, axis=0)
                continue
        elif incm == '':
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue

        try:
            int(row['hcl'][1:], 16)
        except:
            dfNoNan = dfNoNan.drop(labels=index, axis=0)
            continue

    # print(dfNoNan)
    print(len(dfNoNan.index))
