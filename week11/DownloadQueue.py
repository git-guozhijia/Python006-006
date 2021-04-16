import os
import requests, queue, threading
from fake_useragent import UserAgent


class DownloadThread(threading.Thread):
    def __init__(self, q):
        super(DownloadThread, self).__init__()
        self.q = q

    def run(self):
        while True:
            url = self.q.get()
            print(f"{self.name} begin download {url}")
            self.download_file(url)
            self.q.task_done()
            print(f"{self.name} download completed")

    def download_file(self, url):
        ua = UserAgent()
        headers = {"User-Agent": ua.random}
        # 当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
        r = requests.get(url=url, stream=True, headers=headers)
        fname = os.path.basename(url) + ".html"
        with open(fname, "wb") as f:
            for chunt in r.iter_content(chunk_size=1024):
                if not chunt:
                    break
                f.write(chunt)


if __name__ == '__main__':
    urls = ["http://www.baidu.com", "http://www.python.org", "http://www.douban.com"]
    q = queue.Queue()
    for i in range(2):
        t = DownloadThread(q)
        t.setDaemon(True)  # 是否可以后台运行，关闭终端后台依然可以运行
        t.start()
    for url in urls:
        q.put(url)
    q.join()
