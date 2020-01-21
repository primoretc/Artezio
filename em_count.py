# -*- coding: utf-8 -*-
# посчитаем число е-маил в рассылке, а следовательно и число зареганых пользователей
# выдерну адреса заключенные в <> и сохраню в новый файл

email = 1  # если есть рассылка, то полагаю, что как минимум один адрес уже есть

inFile = open('email_list.txt', 'r') # открываю файл исходник, полученый копипастой из заголовка письма <To:>
outFile = open("out_email.txt", "w") # открываю файл в который буду собирать адреса

# бегу по строчкам файла 
for line in inFile:
    
    s1 = line.find("<")
    s2 = line.rfind(">")
    adress = line[s1+1:s2] 
    
    outFile.write(adress + "\n")
    # бегу по символам строки...
    for simvol in line:
        if simvol == ",":
            email += 1
            
# всё закрываю
inFile.close()
outFile.close()

print(f"Число зарегавшихся: {email}")

