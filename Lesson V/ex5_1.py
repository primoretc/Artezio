'''
Разработать класс Complex, которые бы описывал комплексные числа, позволял их
складывать, вычитать, умножать, делить и получать модуль.
Вывод действительной и мнимой частей должен быть с точностью до двух знаков после
запятой.
На вход: действительная и мнимая часть числа, разделенная пробелом.

На выходе:
Для двух комплексных чисел вывод должен быть в следующей последовательности в
отдельных строках:
C + D
C – D
C * D
C/D
mod(C)
mod(D)

P.S. Не забудьте про перегрузку магических методов, пожалуйста

'''
from math import sqrt
class Complex(object):
    
    def __init__(self, x=0, y=0):
        self.real = x
        self.image = y
    # сумма
    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)
    # разность
    def __sub__(self, other):
        return Complex(self.real - other.real, self.image - other.image)
    # умножение
    # (a+bi)*(c+di) = (ac-bd) + (bc+ad)i        
    def __mul__(self, other):
        
        return Complex(self.real * other.real - self.image*other.image, self.image * other.real + self.real * other.image)
    # деление
    # (a+bi)   ac + bd    bc-ad
    #------- = ------- + --------
    # (c+di)   cc + dd    cc+dd
    def __truediv__ (self, other):
        res_real = (self.real * other.real + self.image * other.image) / (other.real ** 2 + other.image ** 2)
        res_image = (self.image * other.real - self.real * other.image) / (other.real ** 2 + other.image ** 2)
        return Complex (res_real, res_image)

    def __abs__(self):                    
        return Complex(sqrt(self.real ** 2 + self.image ** 2) , 0)

    def __str__(self):
        if self.image >=0:
            return '{:.2f}+{:.2f}i'.format(self.real, self.image)
        else:
            return '{:.2f}{:.2f}i'.format(self.real, self.image)    
    
    


#c = Complex(2, 1)
#d = Complex(5, 6)

cStr = input("Введите действительную и мнимую часть Первого числа, разделенная пробелом ")
cL = cStr.split(" ")
c= Complex(int(cL[0]), int(cL[1]))

cStr = input("Введите действительную и мнимую часть ВТОРОГО числа, разделенная пробелом ")
cL = cStr.split(" ")
d= Complex(int(cL[0]), int(cL[1]))


print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(abs(c))
print(abs(d))



