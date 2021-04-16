from multiprocessing import Queue, Process


def f(q):
    string = 'x' * 1000
    print(f"子进程推送队列数据：{string}")
    q.put(string)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
    p.terminate()
    # 会造成死锁，队列内没有数据之后再去获取数据，获取数据的时候一直在等待数据，造成死锁
    # print(q.get())