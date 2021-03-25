from multiprocessing import Process
import time


def run():
    print("子进程开始")
    time.sleep(2)
    print("子进程结束")


if __name__ == '__main__':
    print("父进程开始")
    p = Process(target=run)
    p.start()
    p.join(timeout=1)
    print("父进程结束")
    # 输出结果：
    # 父进程开始
    # 子进程开始
    # 父进程结束
    # 子进程结束

    # print("父进程开始")
    # p = Process(target=run)
    # p.start()
    # p.join()
    # print("父进程结束")
    # # # 输出结果
    # # 父进程开始
    # # 子进程开始
    # # 子进程结束
    # # 父进程结束
