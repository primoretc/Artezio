from website_alive.check_response import chk_res


url = input("Введите адрес сайта: ")
#url="http://google.ru"


if chk_res(url):
    print("Site alive!")
else:
    print("Site down!")
