from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor


def response(*args, **kwargs):
    print("返回网页内容")


def callback(*args):
    print("执行一个回调", args)


@defer.inlineCallbacks
def start(url):
    d = getPage(url.encode("utf-8"))
    d.addCallback(response)
    d.addCallback(callback)
    yield d


def stop(*args, **kwargs):
    reactor.stop()


if __name__ == '__main__':
    urls = ['http://www.baidu.com', 'http://www.sougou.com']
    li = []

    for url in urls:
        ret = start(url)
        li.append(ret)

    d = defer.DeferredList(li)
    d.addBoth(stop)
    reactor.run()
