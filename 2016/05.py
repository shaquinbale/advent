import hashlib
number = 0
counter = 0
input = "ugkcyxxp"
password = ['', '', '', '', '', '', '', '']
hashlist = ['0', '1', '2', '3', '4', '5', '6', '7']

while counter < 8:
    rawkey = input + str(number)
    key =  hashlib.md5(rawkey.encode()).hexdigest()

    if key.startswith('00000') and key[5] in hashlist and password[int(key[5])] == '':
        password[int(key[5])] = [key[6]]
        counter += 1

    number += 1

print(password)

# this is crap and doesnt really output correctly but it still works
