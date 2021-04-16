from multiprocessing import Process
import os
n = 100  # 在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了


def work():
    global n
    n = 0
    print('子进程内: ', n)  # 子进程内:  0


if __name__ == '__main__':
    # p = Process(target=work)
    # p.start()
    # p.join()
    # print('主进程内: ', n)  # 主进程内:  100
    print(os.path.dirname(__file__))