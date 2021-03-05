def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print(f'[CONSUMER] Consuming {n}...')
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print(f'[PRODUCER] Producing {n}...')
        r = c.send(n)
        print(f'[PRODUCER] Consumer return: {r}')
    c.close()


# c = consumer()
# produce(c)

"""
注意到consumer函数是一个generator，把一个consumer传入produce后：
首先调用c.send(None)启动生成器；
然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
consumer通过yield拿到消息，处理，又通过yield把结果传回；
produce拿到consumer处理的结果，继续生产下一条消息；
produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
最后套用Donald Knuth的一句话总结协程的特点：“子程序就是协程的一种特例。”
"""
# 廖雪峰例子
import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


# loop = asyncio.get_event_loop()  # 获取EventLoop:
# loop.run_until_complete(hello())  # 执行coroutine
# loop.close()


# 廖雪峰例子
import threading
import asyncio


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


# loop = asyncio.get_event_loop()
# tasks = [hello(), hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# 廖雪峰例子
import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print(f"{host} header >>>>>>>> {line.decode('utf-8').rstrip()}")
    writer.close()


# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


