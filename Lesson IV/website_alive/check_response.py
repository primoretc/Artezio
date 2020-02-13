from website_alive.make_request import mk_req
def chk_res(url):
    res = mk_req(url)
    return res.status_code == 200

