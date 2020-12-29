import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

url = 'https://movie.douban.com/top250'

response = requests.get(url=url, headers=headers)

print(response.text)
print(f"接口请求返回的code码：{response.status_code}")