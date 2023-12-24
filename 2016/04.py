import collections as co, re

with open('input4.txt') as file:
    file = file.read().split('\n')

enames = [s[:-11].replace('-', '') for s in file]
IDsum = 0


def checksum(string):  # this is trash code and i hate that i'm using it
    result = ''
    lettercounts = co.Counter(string)
    sortedletters = dict(sorted(lettercounts.items()))
    mostcommon = co.Counter(sortedletters).most_common(5)
    for tuple in mostcommon:
        result += tuple[0]
    return result

for i in range(len(enames)):
    if checksum(enames[i]) == file[i][-6:-1]:
        IDsum += int(file[i][-10:-7])
print(f'The sum of every real sector ID is {IDsum}')


decoded = []

for string in file:
    str = ''
    for c in string[:-11]:
        c = chr((((ord(c) - 96) + int(string[-10:-7])) % 26) + 96)  # this is an affront to god
        str += c
    decoded.append(str)
for i in range(len(decoded)):
    if "north" in decoded[i]:
        print(f'The sector ID that contains the North Pole objects is {file[i][-10:-7]}')