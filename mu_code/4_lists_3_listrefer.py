#liste nicht modifiziert

eggs = [1, 2, 3]

spam = eggs
eggs = [4, 5, 6]
print(spam)


# liste modifiziert
eggs = [1, 2, 3]
spam = eggs
for i in range(len(eggs)):
    eggs[i] = 4 + i
print('spam', spam)