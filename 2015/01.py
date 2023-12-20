data = open("input.txt").read()
floor = 0
bcheck = 0
# part 1
for character in data:
    if character == "(":
        floor += 1
    elif character == ")":
        floor -= 1
print(floor)

# part 2
for i in range(len(data)):
    if data[i] == "(":
        bcheck += 1
    elif data[i] == ")":
        bcheck -= 1
    if bcheck < 0:
        print(i+1)
        break
