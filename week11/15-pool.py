from multiprocessing import Pool
from time import time, sleep
import os, random


def run(name):
    print(f"{name}--子进程开始运行,子进程ID：{os.getpid()}")
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print(f"{name}--子进程运行结束,子进程ID：{os.getpid()}， 耗时：{end - start}")


if __name__ == '__main__':
    print("父进程开始")
    # 创建多个进程
    p = Pool(4)
    for i in range(10):
        # 创建进程，并放入进程池统一管理，这是异步方式创建进程，直接使用p.apply(func=run, args=(f"name:{i}",))就是同步方式
        p.apply_async(func=run, args=(f"name:{i}",))
    # 如果我们使用的是进程池，在调用join()之前需要先调用close()
    # 在调用close()之后，不能再向进程池添加新的进程了
    # 当调用close()函数的时候，子进程中有任务在执行，close()会等待任务去结束
    p.close()
    # 进程池调用join()函数，会等待进程池内所有的子进程结束完毕之后再去结束父进程
    p.join()
    # 直接关闭进程池
    p.terminate()
    print("父进程结束")
