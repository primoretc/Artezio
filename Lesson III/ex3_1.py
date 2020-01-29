'''
1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или кортеж) целых чисел.
     - первая функция должна вернуть квадраты элементов коллекции;
     - вторая функция должна вернуть только элементы на четных позициях;
     - третья функция возвращает кубы четных элементов на нечетных позициях.

'''

sp = [2, 44, 1, 25, 8, 12, 67, 2, 4, 6]
tp = (2, 44, 1, 25, 8, 12, 67, 2, 4, 6)

# - первая функция должна вернуть квадраты элементов коллекции;
def kvel(x):
    res = []
    for i, el in enumerate(x):
        res.append(el**2)
    print(res) 

# - вторая функция должна вернуть только элементы на четных позициях;
def chel(x):
    res = []
    for i, el in enumerate(x):
        if i%2 == 0 and i>0 :
            res.append(el)
    print(res) 

#- третья функция возвращает кубы четных элементов на нечетных позициях.
def kubel(x):
    res = []
    for i, el in enumerate(x):
        if i%2 != 0 and el%2 == 0 :
            res.append(el**3)
    print(res) 


kvel(sp)
kvel(tp)

chel(sp)
chel(tp)

kubel(sp)
kubel(tp)
