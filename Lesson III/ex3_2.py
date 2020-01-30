'''
2. Написать функцию, которая принимает произвольное количество любых аргументов. 
    Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи. 
    Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
    Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел. 
    Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a) 
    При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.
'''
#z = (1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))

def nsum(*args, **kwargs):
    product = 1
    suma = 0
    # def wtf(x, pr, su):
    #     if isinstance(x,int):                   # если элемент число, то делаем сумму и произведение
    #         pr = pr * x
    #         print(f"product = {pr}")
    #         su = su + x
    #         print(f"suma = {su}")
    #         return x, pr, su
    #     elif isinstance(x,list):                # если элемент список то берем по одному элемиенту из него
    #         for k, i in enumerate(x):
    #             print (f"x = {x}")
    #             wtf(x, pr, su )
    def wtf(i):    
        if isinstance(i,int):                   # если элемент число, то делаем сумму и произведение
            nonlocal product
            nonlocal suma
            if i != 0: 
                product = product * i
            print(f"product = {product}")
            suma = suma + i
            print(f"suma = {suma}")
            return i
        elif isinstance(i,list):                # если элемент список то берем по одному элемиенту из него
            for k, i in enumerate(i):
                wtf(i)
        elif isinstance(i,tuple):                # если элемент кортеж то берем по одному элемиенту из него
            for k, i in enumerate(i):
                print (f"i = {i} type = {type(i)}")
                wtf(i)                

    for i in args:
        wtf(i)

    for k, value in kwargs.items():
        print(k, value)

    return product, suma
        

nsum(1, 2, 10, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))