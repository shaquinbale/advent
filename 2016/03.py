import re

with open('input3.txt') as file:
    file = file.read()

triangles = [[int(num) for num in line.split()] for line in file.split('\n')] # sorting the list
possible = 0

# part 1
for line in triangles:
    line = sorted(line)
    if line[0] + line[1] > line[2]:
        possible += 1
print(f'There are {possible} possible triangles in your old list.')

newtri = []
possible = 0
# part 2
for column in range(3):
    for i in range(int(len(triangles) / 3)):
        list = []
        i = i * 3
        list.append(triangles[i][column])
        list.append(triangles[i + 1][column])
        list.append(triangles[i + 2][column])
        newtri.append(list)

for line in newtri:
    line = sorted(line)
    if line[0] + line[1] > line[2]:
        possible += 1
print(f'There are {possible} possible triangles in your new list.')