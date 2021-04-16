from multiprocessing import Pool
import os,time
import random


def func01(num):
    w = [str(num), str(num + 1), str(num + 2)]
    print(f"func01()：当前运行进程号：{os.getpid()}，父进程：{os.getppid()}， 返回值w：{w}")
    return w


def func02(x):
    print(f"func02()：当前运行进程号：{os.getpid()}，父进程：{os.getppid()}，参数x：{x}")
    time.sleep(random.random() * 3)
    print(1)
    with open("test.txt", "a") as f:
        for i in x:
            f.write(str(i))
        f.write('\n')


if __name__ == '__main__':
    print(f"父进程：{os.getppid()}")
    p = Pool(processes=4)
    for i in range(10):
        # print(p.apply_async(func01, (i,), callback=func02).get())
        # print(p.apply_async(func02, ([1,1,2,3,43],)).get())
        p.apply_async(func02, ([1, 1, 2, 3, 43],))
    p.close()
    p.join()
    p.terminate()
