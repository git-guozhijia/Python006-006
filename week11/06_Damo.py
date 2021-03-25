from multiprocessing import Process
from time import sleep

num = 100


def run():
    print("子进程开始")
    global num
    print(num)
    print(f"子进程num：{num}")
    print("子进程结束")


if __name__ == '__main__':
    print("父进程开始")
    p = Process(target=run)
    p.start()
    p.join()
    print(f"父进程结束. num：{num}")
