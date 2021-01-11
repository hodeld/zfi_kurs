set1 = {1, 2, 3}
set1.add(1)
print(set1)
set2 = set()
set2.add(1)
try:
    set2[0]
except TypeError:
    pass

if 1 in set2:
    set2.remove(1)
print(set2)