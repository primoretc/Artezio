from website_alive.check_response import chk_res


#url = input("Введите адрес сайта: ")
url="http://google.ru"

print(chk_res(url))
if chk_res(url):
    print("Site alive!")
else:
    print("Site down!")
