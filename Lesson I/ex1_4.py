"""
4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
inList = ['c','abc', 'xyz', 'aba', '1221', '55', '34564gfhd3', 'казак']
k = 0
for i in inList:
    if len(i) >=2 :
        if i[0]==i[-1]:
            k+=1
            print(i)
print (k)

