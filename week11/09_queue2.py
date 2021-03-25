from multiprocessing import Process, Queue
import os, time


def write(q):
    print(f"write子进程启动：{os.getpid()}")
    for i in [1, 2, 3, 4]:
        print(f"queue 写入 {i}")
        q.put(i)
        time.sleep(1)
    print(f"write子进程结束：{os.getpid()}")


def read(q):
    print(f"read子进程启动：{os.getpid()}")
    if_while = True
    while if_while:
        value = q.get(True)
        print(f"read func 获取queue value：{value}")
    print(f"read子进程结束：{os.getpid()}")


if __name__ == '__main__':
    # 两个子进程之间的通讯
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

    print("父进程结束")
