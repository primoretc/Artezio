"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
inStr = input("Введите произвольную строку: ")
outStr = ""

if len(inStr) < 2:
    outStr = ""
else:
    s1 = inStr[0:2]    
    s2 = inStr[-2:-1]
    outStr = s1 + s2

print(outStr)
