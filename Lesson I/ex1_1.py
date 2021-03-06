"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalized correctly as Alison Heck. 
Given a full name, your task is to capitalize the name appropriately. 
Input Format:A single line of input containing the full name, S.
Constraints:* 0 < len(S) < 1000* 
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. 
Example 12abc when capitalized remains 12abc.
Output Format:Print the capitalized string, S.
"""

FullName = input("Введите полное имя: ")

s = ""

if len(FullName) > 0 and len(FullName) < 1000:
    sn = FullName.split(" ") 
    for i in sn:
        if i.isdigit(): # если трока содержит цифры, то ничего с ней не делаем
            s+=i
            s=s+ " "    # добавляю в результирующую строку пробел (<space>) , чтобы не склеивать рядом стоящие отдельные слова
        else:
            s+=i.capitalize()    # превый символ перевожу в верхний регистр остальные в нижний
            s=s + " "    # добавляю в результирующую строку пробел (<space>) , чтобы не склеивать рядом стоящие отдельные слова
    print(s.rstrip()) # просто удаляю самый правый пробел (<space>)
 
else:
    print("Введенное имя имеет некорректное количество символов")

