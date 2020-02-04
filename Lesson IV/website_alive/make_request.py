# make_request
import requests as re
def make_request(url):
    req = re.request('GET', url)
    return req


#print(make_req("http://google.ru"))