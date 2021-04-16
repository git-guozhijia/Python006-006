import threading
import time

# RLock允许在同一线程中被多次acquire(多次上锁和多次解锁的情况下)
mutex = threading.RLock()

num = 0

class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire(blocking=True):
            global num
            time.sleep(1)
            num += 1
            print(self.name,'----num:',num)
        mutex.release()

if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()