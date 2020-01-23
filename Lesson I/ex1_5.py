"""
5. You are given with 3 sets, find if third set is a subset of the first and the second sets
Input: set([1,2]), set([2,3), set([2])
Expected result: True
Input: set([1,2]), set([3,4), set([5])
Expected result: False
"""
a = set([1,2])
b = set([2,3])
c = set([2])


if c.issubset(a) and c.issubset(b):
    print (True)
else:
    print (False)


a = set([1,2])
b = set([3,4])
c = set([5])

if c.issubset(a) and c.issubset(b):
    print (True)
else:
    print (False)