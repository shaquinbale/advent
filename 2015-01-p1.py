data = open("2015input.txt").read()
floor = 0
for character in data:
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1
print(floor)