from lxml import etree
import requests
from queue import Queue
import json
import threading
from fake_useragent import UserAgent
# https://www.jianshu.com/p/74bce9140934

user_agent = UserAgent(verify_ssl=False)

class CrawlThread(threading.Thread):
    # 定义爬虫类
    def __init__(self, thread_id, queue):
        threading.Thread.__init__(self)
        # self.thread_id 给每个进程添加一个标识，类似于名字
        self.thread_id = thread_id
        self.queue = queue
        self.headers = {
            "User-Agent": user_agent.random
        }

    def run(self):
        print(f"启动线程：{self.thread_id}")
        self.scheduler()
        print(f"关闭线程：{self.thread_id}")

    # 定义爬虫类内的爬虫方法
    def scheduler(self):
        # self.queue.empty()判断队列是否为空，为空则返回true
        while not self.queue.empty():
            # 获取网页的队列，需要通过get()方法获取，队列内存储的是页码
            # Queue.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；
            # 1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；
            # 2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；
            page = self.queue.get()
            print(f"下载线程：{self.thread_id}, 下载页面：{page}")
            url = f"https://movie.douban.com/top250?start={page * 25}"
            try:
                response = requests.get(url, headers=self.headers)
                # 判断请求豆瓣页面是否正常
                if response.status_code == 200:
                    # 每次请求豆瓣页面的返回数据存储进dataQueue队列内
                    dataQueue.put(response.text)
                else:
                    continue
            except Exception as err:
                print(f"下载文件出现异常：{err}")

class ParserThread(threading.Thread):
    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f"启动线程：{self.thread_id}")
        # flag变量在运行run方法前设置变量为true
        # while flag:
        #     try:
        #         self.queue.qseiz()
        #         item = self.queue.get(False)
        #         if not item:
        #             continue
        #         self.parse_data(item)
        #         self.queue.task_done()
        #     except Exception as err:
        #         pass
        while not self.queue.empty():
            try:
                print("队列不为空")
                item = self.queue.get(False)
                self.parse_data(item)
                self.queue.task_done()
            except Exception as err:
                pass
        print(f"结束线程：{self.thread_id}")

    def parse_data(self, item):
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="hd"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')
                    link = book.xpath('./a/@href')
                    response = {
                        'title': title,
                        'link': link
                    }
                    # print(response)
                    json.dump(response, fp=self.file, ensure_ascii=False)
                except Exception as err:
                    print(f'book error:{err}')
        except Exception as err:
            print(f'page error:{err}')

if __name__ == "__main__":
    # 定义存放网页的任务队列
    pageQueue = Queue(20)
    for page in range(0, 5):
        # 获取豆瓣数据需要循环10次
        pageQueue.put(page)
    # 定义存放解析数据的任务队列
    dataQueue = Queue()

    # 爬虫线程
    crawl_threads = []
    crawl_name_list = ['crawl01', 'crawl02', 'crawl03']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id=thread_id, queue=pageQueue)
        thread.start()
        crawl_threads.append(thread)
        print(crawl_threads)



    with open('book.json', 'a', encoding='utf-8') as pipeline_f:
        # 存放即将创建的进程
        parse_thread = []
        # 创建解析网页数据的进程名称列表
        parser_name_list = ['parse_01', 'parse_02', 'parse_03']
        import time
        time.sleep(3)
        flag = True
        for thread_id in parser_name_list:
            thread = ParserThread(thread_id, dataQueue, pipeline_f)
            thread.start()
            parse_thread.append(thread)
        for crawl in crawl_threads:
            crawl.join()
        flag = False
        for t in parse_thread:
            t.join()

    print("退出主进程！")



