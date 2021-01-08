#1
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')


#2
name = 'Mary'
print('enter password')
password = input()
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    elif password == 'Mary':
        print('nice try')
    else:
        print('Wrong password.')