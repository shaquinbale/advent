with open("input.txt") as file:
    sum = 0
    for line in file.readlines():
        for character in line:
            if character.isdigit():
                sum += int(character) * 10
                break
        for character in line[::-1]:
            if character.isdigit():
                sum += int(character)
                break

print(sum)