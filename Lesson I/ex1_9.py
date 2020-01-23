"""
9. Write a Python program to remove duplicates from a list.

"""
l = [1,3,4,3,1,56,1,56,234]
print(l)
for i in l:
     if  l.count(i)>=2:
        l.remove(i)
print(l)