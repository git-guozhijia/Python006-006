import os

res = os.fork()

print(f"res == {res}")

if res == 0:
    print(f"我是子进程，我的进程id是{os.getpid()}， 我的父进程id是{os.getppid()}")
else:
    print(f"我是父进程，我的进程id是{os.getpid()}")

# 执行结果：
# res == 20090
# 我是父进程，我的进程id是20089
# res == 0
# 我是子进程，我的进程id是20090， 我的父进程id是20089

"""
fork()运行是，会有两个返回值，返回值大于0时，此进程为父进程，且返回的数字为子进程的PID；当返回值为0的时候就是子进程
# 父进程结束时，子进程不会随着父进程结束立刻结束，同样，父进程不会等待子进程执行完
# os.fork()无法在windows系统上运行
"""
