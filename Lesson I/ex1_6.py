"""
6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
"""
d = {}
n = input("Число элементов словаря: ")
n = int(n)
i=1
while i <= n:
    d[i] = i**2
    i+=1

print(d)  

