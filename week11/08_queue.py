from multiprocessing import Process, Queue, Value


def w(q, value):
    q.put(value)


def r(q):
    value = q.get()
    return value


if __name__ == '__main__':
    """
    # 子进程和父进程之间的通讯
    q = Queue()
    p = Process(target=run, args=(q,))
    p.start()
    # Queue.get(block=True, timeout=None)
    # block参数为True的时候，且timeout不为None，就会阻塞等待向队列获取数据，反之，直接报出异常
    print(q.get())
    p.join()
    """

    q = Queue()

    p1 = Process(target=w, args=(q,))
    p2 = Process(target=r, args=(q,))

    # p.start()
    # Queue.get(block=True, timeout=None)
    # block参数为True的时候，且timeout不为None，就会阻塞等待向队列获取数据，反之，直接报出异常
    # print(q.get())
    # p.join()
