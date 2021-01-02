import requests
# pip install lxml
from lxml import etree
from time import sleep
from datetime import datetime
from pathlib import Path

def get_url_name(myurl):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    headers = {'User-Agent':ua}
    response = requests.get(myurl, headers=headers)

    if response.status_code == 200:
        selector = etree.HTML(response.text)
        film_name = selector.xpath('//*[@class="hd"]/a/span[1]/text()')
        film_link = selector.xpath('//*[@class="hd"]/a/@href')
        film_info = dict(zip(film_name, film_link))
        for i in film_info.items():
            print(f"电影名称：{i[0]}\t\t\t\t 电影链接：{i[1]}")
            sleep(0.1)
            with open(str(P), 'a') as a:
                a.write(f"电影名称：{i[0]}\t\t\t\t 电影链接：{i[1]}\n")

if __name__ == '__main__':
    p = Path(__file__).parent.resolve()
    path = Path.joinpath(p, Path(f'./html'))
    if not path:
        path.mkdir()
    P = Path.joinpath(p, Path(f'./html/{datetime.now().strftime("%Y-%m-%d")}.txt'))
    if not P.is_file():
        P.touch()
    urls = tuple(f"https://movie.douban.com/top250?start={page * 25}" for page in range(10))
    for url in urls:
        get_url_name(url)
        sleep(3)

