file = open('input.txt').read()

# part 1
houses = [(0, 0)]
x, y = 0, 0

for i in range(len(file)):
    if file[i] == '^':
        y += 1
    elif file[i] == 'v':
        y -= 1
    elif file[i] == '<':
        x -= 1
    elif file[i] == '>':
        x += 1
    houses.append((x, y))


print(len(set(houses)))
# part 2
sx, sy, rx, ry = 0, 0, 0, 0
houses2 = [(0, 0)]

for c in file[0::2]:
    if c == '^':
        ry += 1
    elif c == 'v':
        ry -= 1
    elif c == '<':
        rx -= 1
    elif c == '>':
        rx += 1
    houses2.append((rx, ry))

for c in file[1::2]:
    if c == '^':
        sy += 1
    elif c == 'v':
        sy -= 1
    elif c == '<':
        sx -= 1
    elif c == '>':
        sx += 1
    houses2.append((sx, sy))

print(len(set(houses2)))


