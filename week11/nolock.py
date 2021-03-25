import datetime
import multiprocessing as mp
import time


def job(v, num, lock):
    for _ in range(5):
        time.sleep(0.4)
        with lock:
            v.value += num  # 设置共享变量的值
        print(v.value, end='--')


def me_job(v, num, lock):
    for _ in range(5):
        with lock:
            v += num
        print(v, end='--')


def me_job_test(v):
    for i in [1,3,5]:
        v += i
    print(v)


if __name__ == '__main__':
    """
    v = mp.Value('i', 0)
    lock = mp.Lock()
    p1 = mp.Process(target=job, args=(v, 1, lock))  # 设定不同的num值
    p2 = mp.Process(target=job, args=(v, 3,lock))
    p3 = mp.Process(target=job, args=(v, 5,lock))
    """

    """
    q.put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
    q.get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常.

    q.get_nowait(): 同q.get(False)
    q.put_nowait(): 同q.put(False)

    q.empty(): 调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。
    q.full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。
    q.qsize(): 返回队列中目前项目的正确数量，结果也不可靠，理由同q.empty()
    和q.full()
    一样
    """
    starttime = datetime.datetime.now()  # 获取当前日期
    a = 100
    v = mp.Value('i', 0)
    lock = mp.Lock()
    p1 = mp.Process(target=me_job, args=(a, 1, lock))  # 设定不同的num值
    p2 = mp.Process(target=me_job, args=(a, 3, lock))
    p3 = mp.Process(target=me_job, args=(a, 5, lock))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    endtime = datetime.datetime.now()
    print('extend执行时间：{0}秒'.format((endtime - starttime).seconds))
    print('extend执行时间：' + str((endtime - starttime).seconds) + "秒")

    starttime = datetime.datetime.now()  # 获取当前日期
    me_job_test(100)
    endtime = datetime.datetime.now()
    print((endtime - starttime).seconds)