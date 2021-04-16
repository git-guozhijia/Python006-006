import threading
import queue
import random
import time

"""
q = queue.Queue(5)

q.put(111)
q.put(222)
q.put(333)

print(q.get())
print(q.get())
print(q.get())

q.task_done()#每次从queue中get一个数据之后，档处理好相关问题，最后调用给方法，以提示q.join()是否停止阻塞，让线程继续执行或者退出

print(q.qsize())  # 判断队列内的元素个数
print(q.empty())  # 队列是否空了
print(q.full())  # 队列是否满了
"""

waitelock = threading.Lock()
num = 0


class Producer(threading.Thread):
    def __init__(self, q, con, name):
        super(Producer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f"Producer {self.name} Started")

    def run(self):
        while True:
            global waitelock
            self.con.acquire()  # 打开条件锁

            if self.q.full():  # 判断队列是否满了，self.con.wait()等待消费者的消息，得到消息之后执行else
                with waitelock:
                    print("Queue is full, producer wait")
                self.con.wait()
            else:
                value = random.randint(1, 10)
                with waitelock:
                    global num
                    num += 1
                    print(f"{self.name} print({num})")
                #     print(f"{self.name} put value ({self.name} : {str(value)}) in queue")
                self.q.put((f"{self.name} : {str(value)}"))
                self.con.notify()  # 通知消费者
                time.sleep(1)
            self.con.release()


class Consumer(threading.Thread):
    def __init__(self, q, con, name):
        super(Consumer, self).__init__()
        self.q = q
        self.con = con
        self.name = name

        print(f"Consumer {self.name} Started")

    def run(self):
        while True:
            global waitelock
            self.con.acquire()
            if self.q.empty():  # 判断队列是否为空
                with waitelock:
                    print("Queue is empty, producer wait")
                self.con.wait()  # 等待资源
            else:
                value = self.q.get()
                with waitelock:
                    global num
                    num += 1
                    print(f"{self.name} print({num})")
                    # print(f"{self.name} get value {str(value)} from queue")
                self.con.notify()  # 通知生产者
                time.sleep(1)
            self.con.release()


if __name__ == '__main__':
    q = queue.Queue(10)

    con = threading.Condition()

    p1 = Producer(q, con, "生产者1--")
    p1.start()
    p2 = Producer(q, con, "生产者2--")
    p2.start()
    c1 = Consumer(q, con, "消费者3--")
    c1.start()
