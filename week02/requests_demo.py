import requests,sys
from pathlib import *

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

url = 'https://movie.douban.com/top250'

try:
    response = requests.get(url=url, headers=headers, timeout=3)
except requests.exceptions.ConnectTimeout as err:
    print("请求超时。")
    sys.exit(1)
except Exception as err:
    print(err)

p = Path(__file__).resolve().parent
html_path = p.joinpath('html')
if not html_path.is_dir():
    html_path.mkdir()
page = html_path.joinpath('douban.html')

try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f"FileNotFoundError：{e}")
except IOError as e:
    print(f"读取文件错误：{e}")
except Exception as e:
    print(e)

