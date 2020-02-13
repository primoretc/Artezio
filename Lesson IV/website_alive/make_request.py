import requests
def mk_req(url):
    req = requests.request('GET', url)
    return req