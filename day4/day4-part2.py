import os, sys, re

validPasswords = set()
increasingPasswords = set()

for password in range(206938,679128):
    password = str(password)
    # Check that the numbers in the string do not decrease
    for key,number in enumerate(password, 0):
        if key == 0:
            continue
        elif int(number) < int(password[key-1]):
            break
    else:
        increasingPasswords.add(password)

for password in increasingPasswords:
    # Check there's at least one set of repeating digits - but with a block size no bigger than 2
    for key,number in enumerate(password, 0):
        if password.count(number) == 2:
            validPasswords.add(password)

print(f'{len(validPasswords)}')
