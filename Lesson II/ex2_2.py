'''
2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’
'''

a = int(input("Введите число A: "))
b = int(input("Введите число B больше A: "))
c = int(input("Введите число C: "))

def acb(x,y,z):
    k = 0
    for i in range(x, y+1):
        if i%c == 0:
            k+=1
            print(i)
    print (f"Число чисел между [a:b] делящихся на c : {k}")

acb(a,b,c)
