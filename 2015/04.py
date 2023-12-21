import hashlib
number = 0
input = "iwrupvqb"

while True:
    rawkey = input + str(number)
    key = rawkey.encode()
    ikey =  hashlib.md5(key).hexdigest()
    if ikey.startswith('000000'):
        break
    number += 1


print(number)