"""
multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}):
    :param group: 分组，实际上很少使用
    :param target: 标识调用对象，你可以传入方法的名字
    :param name: 别名，相当于给这个进程设置一个名字
    :param args: 表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入（m，n）
    :param kwargs: 表示调用对象的字典
"""

from multiprocessing import Process
import time, os


def f(name):
    # time.sleep(5)
    print(f"{os.getpid()}   f")
    print(name)


if __name__ == '__main__':
    p = Process(target=f, args=('zzh',))
    print(f"{os.getpid()}", 222)

    p.start()
    p.join(timeout=None)

    print(f"{os.getpid()}", 222)
    # join()函数，父进程需要等待子进程结束之后，再去结束，如果子进程一直不结束，join()函数可以设置timeout参数，设置多少秒之后父进程强制结束，不在等待子进程
