import re

file = open("day5input.txt").read()
strings = file.split()

# part 1
vowels = re.compile(r'[aeiou].*[aeiou].*[aeiou]')
forbidden = re.compile(r'ab|cd|pq|xy')
doubles = re.compile(r'(.)\1')
naughty = 0

for s in strings:
    if doubles.search(s) is None:  # doubled letters
        naughty += 1
    elif vowels.search(s) is None:  # three vowels
        naughty += 1
    elif forbidden.search(s):  # forbidden pairs
        naughty += 1
print(len(strings) - naughty)

#part 2
pairsoftwo = re.compile(r'(..).*\1')
interruptedpair = re.compile(r'(.)(.)\1')
nice = 0

for s in strings:
    if pairsoftwo.search(s) and interruptedpair.search(s):
        nice +=1
print(nice)