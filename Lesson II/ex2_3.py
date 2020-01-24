'''
3. Написать функцию вычисления факториала числа
'''

n = int(input("Введите число: "))

def fact(x):
    f = 1
    for i in range(1, x+1):
        f = f * i
    print(f)


fact(n)
