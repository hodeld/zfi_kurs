# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():

        print(v, k)
    print("Total number of items: " + str(item_total))


def displayInventory2(inventory, catname=''):
    print("Inventory:", catname)
    item_total = 0
    for k, v in inventory.items():
        end = ''
        if v > 1:
            end = 's'
        print(v, k + end)
    print("Total number of items: " + str(item_total))


displayInventory(stuff)

# Quaratett
stuff = {'Länge': 9, 'Breite': 2, 'Farbe': 2, 'Geschmack': 4, 'Konsistenz': 3} # Karotte
stuff2 = {'Länge': 4, 'Breite': 4, 'Farbe': 2, 'Geschmack': 3, 'Konsistenz': 5}  #

print('Gemüse', '-Quartett')
catname = 'Tomate'
displayInventory2(stuff2)
while True:
    print('Wähle deine Kategorie oder Nichts')
    cat = input()
    if cat == '':
        break
    while True:
        if cat in stuff2:
            break
        print(cat, 'nicht dabei.', 'Wähle deine Kategorie')
        cat = input()

    val2 = stuff2[cat]

    val1 = stuff[cat]

    if val2 >= val1:
        print('you win')
    else:
        print('you loose')