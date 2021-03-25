from multiprocessing import Process
import os, time


class NewPerocess(Process):
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):
        while True:
            print(f"我是进程：name：{self.num}， id：{os.getpid()}, 我的PID是：{os.getppid()}")
            time.sleep(1)


if __name__ == '__main__':

    for i in range(2):
        p = NewPerocess(i)
        p.start()
