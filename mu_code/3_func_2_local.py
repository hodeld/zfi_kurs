#Local Variables Cannot Be Used in the Global Scope
def spam():
    eggs = 31337
spam()
print(eggs)

#Code in a function’s local scope cannot use variables in any other local scope
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    print(eggs)

spam()

#use global local
#Code in a function’s local scope cannot use variables in any other local scope
eggs = 'global_eggs'
def spam():
    print(eggs)

spam()

#same name
eggs = 'global eggs'
def spam():
    eggs = 'local eggs'
    print(eggs)

spam()
print(eggs)

#global statement
def spam():
    global eggs
    eggs = 'local eggs'
    print(eggs)

eggs = 'global'
print(eggs)
spam()
print(eggs)

#nonlocal statement
def spam():
    eggs = 'global eggs'
    print(eggs)
    def inner_spam():
        nonlocal eggs
        eggs = 'local eggs'
        print(eggs)
    inner_spam()
    print(eggs)

spam()

#WICHTIG -> ohne assign fktioniert
def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()
