with open('input2.txt') as file:
    file = file.read().split('\n')

numpad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

instr = {"U": (0, -1), "D": (0, 1),
         "L": (-1, 0), "R": (1, 0),
         }

pos = (1, 1)
passcode = ''
#part 1
for line in file:
    for cmd in line:
        new_pos = (pos[0] + instr[cmd][0], pos[1] + instr[cmd][1])
        if new_pos[0] < 0 or new_pos[0] > 2 or new_pos[1] < 0 or new_pos[1] > 2:  # if new_pos takes you out of bounds
            continue
        else:
            pos = new_pos
    passcode += str(numpad[pos[1]][pos[0]])
print(f'The passcode, as you imagined it, is {passcode}.')

numpad = [
    [" ", " ", "1", " ", " "],
    [" ", "2", "3", "4", " "],
    ["5", "6", "7", "8", "9"],
    [" ", "A", "B", "C", " "],
    [" ", " ", "D", " ", " "]
]

pos = (2, 0)
passcode = ''
#part 2
for line in file:
    for cmd in line:
        new_pos = (pos[0] + instr[cmd][0], pos[1] + instr[cmd][1])
        if new_pos[0] < 0 or new_pos[0] > 4 or new_pos[1] < 0 or new_pos[1] > 4 or numpad[new_pos[1]][new_pos[0]] == " " :
            continue
        else:
            pos = new_pos
    passcode += str(numpad[pos[1]][pos[0]])
print(f'The real passcode is {passcode}.')