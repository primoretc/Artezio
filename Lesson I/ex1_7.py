"""
7. Write a Python script to merge two Python dictionaries
"""

# этот способ у меня работает на python3.7
d1 = {'a':1, 'z':2, 'h':3}
d2 = {'w':4, 'c':2}
z = {**d1, **d2}

print(z)
z.clear()  # перед применением второго способа очищу словарь, для самоуспокоения ))
print(z)

# можно функцией

def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z

z = merge_two_dicts(d1, d2)
print (z)    