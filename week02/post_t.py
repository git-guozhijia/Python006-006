import requests

'''
'http协议 GET'
g = requests.get('https://github.com')
print(g.status_code)
print(g.headers)
# print(g.encoding)
# print(g.text)

# {'date': 'Tue, 29 Dec 2020 07:44:32 GMT', 'content-type': 'text/html; charset=utf-8', 'server': 'GitHub.com', 'status': '200 OK', 'vary': 'X-PJAX, Accept-Encoding, Accept, X-Requested-With, Accept-Encoding', 'etag': 'W/"36607c073b66c49a388ded745d8812d0"', 'cache-control': 'max-age=0, private, must-revalidate', 'strict-transport-security': 'max-age=31536000; includeSubdomains; preload', 'x-frame-options': 'deny', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'referrer-policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'expect-ct': 'max-age=2592000, report-uri="https://api.github.com/_private/browser/errors"', 'content-security-policy': "default-src 'none'; base-uri 'self'; block-all-mixed-content; connect-src 'self' uploads.github.com www.githubstatus.com collector.githubapp.com api.github.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com cdn.optimizely.com logx.optimizely.com/v1/events wss://alive.github.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com; frame-ancestors 'none'; frame-src render.githubusercontent.com; img-src 'self' data: github.githubassets.com identicons.github.com collector.githubapp.com github-cloud.s3.amazonaws.com *.githubusercontent.com customer-stories-feed.github.com spotlights-feed.github.com; manifest-src 'self'; media-src github.githubassets.com; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; worker-src github.com/socket-worker-5029ae85.js gist.github.com/socket-worker-5029ae85.js", 'Content-Encoding': 'gzip', 'Set-Cookie': '_gh_sess=cPbRLXQohR%2BFGixejz0OFL93BzqMDMYKJjP6oMBZFReWIUvncMRdT%2FK75SQe5dN6Wrmy5VuAlJoHSB6IGCfeLorPG%2FN3ntz6yCs0p%2FDog6IsApHSeY8GVYqKrjcRzs93ehsbgAPyaKVwUEzRxkkFWiOaWsSbwaQZHjFpe6KWnwcFFEFRCzYtuOEMqEfICM3sMEX3Bqc3epd054TCWY7N3FWge1shvOMRAXr11ks4Z6sK9CRDCrhNxyg7BPzPoCZlF6LctusJ2Tph7oL%2BxM0uVw%3D%3D--krF6gI%2BJAjmE7y3f--d2ScFJpTEvEj%2B6Qk2g%2F9TQ%3D%3D; Path=/; HttpOnly; Secure; SameSite=Lax, _octo=GH1.1.1631536245.1609227875; Path=/; Domain=github.com; Expires=Wed, 29 Dec 2021 07:44:35 GMT; Secure; SameSite=Lax, logged_in=no; Path=/; Domain=github.com; Expires=Wed, 29 Dec 2021 07:44:35 GMT; HttpOnly; Secure; SameSite=Lax', 'Accept-Ranges': 'bytes', 'Transfer-Encoding': 'chunked', 'X-GitHub-Request-Id': 'C3CE:7632:2B00FDC:38CA110:5FEADE63'}


'http协议 POST'
url = 'http://httpbin.org/post'
param = {'param01':'value'}
p = requests.post(url=url, data=param)

print(p.json())
print(p.json()['headers'])
print(p.status_code)
'''


# 在同一个session实例下发出的所有请求保持cookie
# 使用session成功的登录了某个网站，则在再次使用该session对象求求该网站的其他网页都会默认使用该session之前使用的cookie等参数
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

import requests
import time
# pip install fake-useragent
from fake_useragent import UserAgent
# https://www.jianshu.com/p/74bce9140934

user_agent = UserAgent(verify_ssl=False)

# print(user_agent.ie)# 随机打印一个 ie 浏览器的头
# print(user_agent.opera)
# print(user_agent.chrome)
# print(user_agent.google)
# print(user_agent.firefox)
# print(user_agent.safari)
# print(user_agent.random)

login_headers = {
    "User-Agent":user_agent.random,
    "Referer":"https://accounts.douban.com/passport/login_popup?login_source=anony"
}
login_param = {
    'ck':'',
    'remember':'true',
    'name':'1729010120033',
    'password':'sdasdad'
}
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
s = requests.Session()
response = s.post(login_url, data=login_param, headers=login_headers)
# print(response.status_code)
# print(response.json())
# print(response.headers.get('User-Agent'))
# print(response.headers)
# print(response.cookies)

if response.status_code == 200:
    url = "https://accounts.douban.com/passport/setting"
    response2 = s.get(url, headers=login_headers)
    print(response2.status_code)
    print(response2.text)
    print(response2)

