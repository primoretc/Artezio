"""
8. Write a Python program to find the highest 3 values in a dictionary
"""

stats = {'a':1000, 'c': 100, 'd': 2000, 'f':2334, 'dd':3300}

def max_three(d):# функция имеет несколько сложный вид, но я так вижу)))
    res = {}
    A = d.copy()
    B = d.copy()
    def max_dict_value(x,y): # функция ищет одно максимальное значение
        z = max(x.values())
        for key, val in x.items(): # будем бежать по словарю и искать это значение, добавлять в новый словарь и удалять пару ключ значение из обрабатываемого, чтобы повторно его крутануть
            if val==z:              
                res[key] = z
                y.pop(key,val)
                return z, y  #возвращаю новый словарь из максимальных значений и копию исходного без этого макисмального значения 
    i=0   
    for i in range(3): #поставлена задача найти 3 максимальных значения словаря 
        pr = max_dict_value(A, B)
        B = pr[1]
        A=B.copy()
        i+=1
    A.clear()
    B.clear()
    return res

print(max_three(stats))

