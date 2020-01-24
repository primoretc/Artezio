"""
9. Write a Python program to remove duplicates from a list.

"""
l = [1,3,4,3,1,56,1,56,234]
#l = [1,2,3,4,5,6,7,8]
#l = ['a','s','a','g']
print(l)

for i in l:
        for k in l:
                if i == k and l.count(i) >=2:
                        l.remove(k)

print(l)

