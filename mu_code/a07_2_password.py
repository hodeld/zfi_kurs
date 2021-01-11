'''
Chapter 7 Pattern Matching with Regular Expressions

Strong Password Detection
'''

import re

passwords = [ 'shortpw', '8charact', 'onlylower', 'ONLYUPPER', 'NoDigitDigit', 'C0rrectPw']


def checkPassword(password):
    print(f'Checking {password}:')
    lengthRegex = re.compile(r'.{8,}') # Length >= 8
    upperLowerRegex = re.compile(r'([a-z])([A-Z])') # At least one upper- and lowercase letter, ( to group
    oneDigitRegex = re.compile(r'\d')
    if lengthRegex.search(password) is None:
        print(f'Password is not long enough. Must be at least 8 characters, {password}: {len(password)}')
        return False
    if upperLowerRegex.search(password) is None:
        print(f'Password must have at least one Uppercase and one lowercase letter, {password}')
        return False
    if oneDigitRegex.search(password) is None:
        print(f'Password must have at least one digit, {password}')
        return False

    return True

for pw in passwords:
    print(checkPassword(pw))