import threading
import time

num = 0

# threading.Lock()的锁mutex.acquire()和mutex.release()是不可以嵌套的
# 也就是说threading.Lock()可以在不同的线程内进行加锁和解锁。可能会出现死锁的情况
mutex = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        # True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这里一直等待到解锁为止
        # False表示非堵塞，即不管本次调用能够成功上锁，都不会卡在这,而是继续执行下面的代码
        if mutex.acquire(blocking=True):
            num += 1
            print(self.name, "线程内的num：", num)
        mutex.release()


if __name__ == '__main__':
    list_thread = []
    for i in range(5):
        t = MyThread()
        t.start()
    for i in list_thread:
        i.join()
