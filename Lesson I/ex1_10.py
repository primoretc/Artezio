"""
10. Write a Python program to get the difference between the two lists

"""

l1 = ['Москва', 'Пекин', 'Торонто', 'Париж']   
l2 = ['Москва', 'Пекин'] 
if len(l1) > len(l2):
    l3 = list(set(l1)-set(l2))
elif  len(l1) < len(l2):
    l3 = list(set(l2)-set(l1))

print (l3)
