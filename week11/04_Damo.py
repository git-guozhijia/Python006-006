from multiprocessing import Process
import os
import multiprocessing


def debug_info(title):
    print("-" * 30)
    print(title)
    print(f"模块名称：{__name__}")
    print(f"父进程ID：{os.getppid()}")
    print(f"当前进程ID：{os.getpid()}")
    print("-" * 30)


def f(name):
    debug_info("function f")
    print(f"hello {name}")


if __name__ == '__main__':
    debug_info("main")
    p = Process(target=f, args=("zzh",))
    p.start()

    for p in multiprocessing.active_children():
        print(f"子进程名称：{p.name}    id：{p.pid}")
    print("进程结束")
    print(f"CPU核心数量：{str(multiprocessing.cpu_count())}")

    p.join()
