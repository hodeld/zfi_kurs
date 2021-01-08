
#1
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

#2 erstellen, dann änderneine ändern
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
while True:
    print('Enter the number of cat ' +
      ' (Or enter nothing to stop.):')
    ind_str = input()
    if ind_str == '':
        break
    ind = int(ind_str) -1

    print('Enter the name of cat ' + ind_str +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '' or :
        break
    catNames[ind] = name

print('The cat names are:')
for name in catNames:
    print('  ' + name)