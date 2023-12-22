import re

with open("input1.txt") as file:
    file = file.read().split(', ')


def digits(string):  # find all digits in a string
    numbers = re.compile(r'\d')
    return int(''.join(numbers.findall(string)))


direction = 0
directions = [0, 0, 0, 0]
location = (0, 0)
visited = set()

for s in file:
    if s[0] == 'R':
        direction += 1
    elif s[0] == 'L':
        direction -= 1

    distance = digits(s)
    directions[direction % 4] += distance

    for _ in range(distance):
        location = (
            location[0] + (direction % 4 == 1) - (direction % 4 == 3),
            location[1] + (direction % 4 == 0) - (direction % 4 == 2)
        )

        if location in visited:
            print(f'The first place you visited is: {abs(location[0]) + abs(location[1])} blocks away')
            exit()  # Exit the loop once the first location visited twice is found

        visited.add(location)

    visited.add(location)





