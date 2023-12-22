import re
import numpy as np

file = open('day6input.txt').read().split('\n')
grid = np.full((1000, 1000), False)
digits = r'\d+'  # find every series of digits in a string

# part 1
for s in file:
    instr = list(map(int, re.findall(digits, s)))
    x1, y1, x2, y2 = instr

    if s.startswith('turn on'):
        grid[x1:x2 + 1, y1:y2 + 1] = True
    elif s.startswith('turn off'):
        grid[x1:x2 + 1, y1:y2 + 1] = False
    elif s.startswith('toggle'):
        grid[x1:x2 + 1, y1:y2 + 1] = (grid[x1:x2 + 1, y1:y2 + 1]) ^ True
print((grid == True).sum())

# part 2
grid = np.full((1000, 1000), 0)
for s in file:
    instr = list(map(int, re.findall(digits, s)))
    x1, y1, x2, y2 = instr

    if s.startswith('turn on'):
        grid[x1:x2 + 1, y1:y2 + 1] += 1
    elif s.startswith('turn off'):
        grid[x1:x2 + 1, y1:y2 + 1] -= 1
        grid = grid.clip(0)
    elif s.startswith('toggle'):
        grid[x1:x2 + 1, y1:y2 + 1] += 2

print(int(np.sum(grid)))
