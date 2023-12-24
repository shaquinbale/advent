from collections import Counter

with open('input6.txt') as file:
    file = file.read().split('\n')

concatenated = ['', '', '', '', '', '', '', '']

#part 1
answer = ''
for column in range(8):
    for line in file:
        concatenated[column] += (line[column])

for i in range(len(concatenated)):
    most_frequent = Counter(concatenated[i]).most_common(1)[0][0]
    answer += most_frequent
print(f'Using the most common letters, the answer is {answer}')

#part 2
answer = ''
for column in range(8):
    for line in file:
        concatenated[column] += (line[column])

for i in range(len(concatenated)):
    most_frequent = Counter(concatenated[i]).most_common()[-1][0]
    answer += most_frequent
print(f'Using the least common letters, the answer is {answer}')