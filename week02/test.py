import requests

a = requests.get('http://www.httpbin.org')

print(a.headers)
print(a.cookies)
# print(a.text)

# {'Date': 'Mon, 28 Dec 2020 06:24:53 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '9593', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}

"""
curl 'https://mpapi.qutoutiao.net/config/getConfig?type=index_banner&token=b7a7tsCBlMe4d2V2hq5-K0b3Yys72mvO4AoXrUsGP9PfYUnWM6K2Fe5ywqy8AgzcM3kWryv410Wyu8M&dtu=200' \
  -H 'Connection: keep-alive' \
  -H 'Pragma: no-cache' \
  -H 'Cache-Control: no-cache' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
  -H 'Origin: https://mp.qutoutiao.net' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://mp.qutoutiao.net/' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  --compressed
"""