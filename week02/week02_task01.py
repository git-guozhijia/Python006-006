import requests,json

page = 0
url = f"https://www.zhihu.com/api/v4/answers/811123830/root_comments?order=normal&limit=20&offset={page}&status=open"
headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
response = requests.get(url,headers=headers)
response = json.loads(str(response.text))
featured_counts = response['featured_counts']
num = 20 - featured_counts
list_m = []
for i in response['data'][featured_counts:]:
    # print(i['content'])
    list_m.append(i['content'])

page = 20
response = requests.get(url,headers=headers)
response = json.loads(str(response.text))
for i in response['data'][:15-len(list_m)]:
    # print(i['content'])
    list_m.append(i['content'])
print(list_m)
with open('zhihu.txt', 'w') as f:
    f.write(str(list_m))

