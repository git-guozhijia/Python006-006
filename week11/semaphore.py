import threading
import time

num = 0


def run(n):
    semaphore.acquire()
    print(f"run the thread: {n}")
    time.sleep(1)
    global num
    num += 1
    print(num)
    semaphore.release()


if __name__ == '__main__':
    # 信号量：内部实现一个计数器，占用信号量的线程的数量超过指定值时自动阻塞
    # 信号量：最多允许5个线程同时运行
    semaphore = threading.BoundedSemaphore(5)
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
