while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')


while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        cap_letter, has_nr = False, False

        for l in password:
            if cap_letter is False:
                cap_letter = l.isupper()
            if has_nr is False:
                has_nr = l.isnumeric()
            if cap_letter and has_nr:
                break
        if cap_letter and has_nr:
            break

    print('Passwords can only have letters and numbers.')
    print('Passwords need to have at least 1 capital letter and 1 number.')

