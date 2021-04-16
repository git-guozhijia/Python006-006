import time, os
from multiprocessing import Pool


def run(x):
    print(f"进程id：{os.getpid()}，父进程id：{os.getppid()}")
    return x * x


if __name__ == '__main__':
    print(f"父进程id：{os.getppid()}")
    # 方式一：apply_async()方法
    # with Pool(processes=4) as poll:
    #     result = poll.apply_async(run, (10,))
    #     print(result.get(timeout=1))
    #     result = poll.apply_async(time.sleep, (0.121,))
    #     print(result.get(timeout=1))  # raise TimeoutError：multiprocessing.context.TimeoutError

    # 方式二：map()和imap()方法，创建进程
    with Pool(processes=4) as pool:
        print(pool.map(run, range(10)))
        it = pool.imap(run, range(10))
        print(it)
        print(next(it))
        print(next(it))
        print(it.next(timeout=1))
        print(list(it))
