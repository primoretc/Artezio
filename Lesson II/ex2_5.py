'''
5. Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с заданным в коде.
	В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
	Если пароль не совпадает, то печатает в консоль 
	"Password for user: <Имя пользователя> is incorrect"
	"Please try again..."
	И снова запрашивает пароль (не завершается).
'''

name = input("Введите имя пользователя: ")
psw =  input("Введите пароль: ")

PASSW = "qwerty"

while True:
    if psw == PASSW:
       print(f"Password for user: {name} is correct") 
       break
    else:
        print(f"Password for user: {name} is incorrect")
        print("Please try again...")
        psw =  input("Введите пароль: ")
        continue

