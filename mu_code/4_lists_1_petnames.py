
#petnames
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


#petnames2
myPets = ['Zophie', 'Pooka', 'Fat-tail']
while True:
    print('Enter a pet name:')
    name = input()
    if name == '':
        break
    if name not in myPets:
        print('I do not have a pet named ' + name)
        myPets = myPets + [name]
    else:
        print(name + ' is my pet.')