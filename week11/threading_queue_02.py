import threading,random,time

num = 0
l = threading.Lock()


class myThread(threading.Thread):
    def run(self):
        self.myTest()
        l.acquire(blocking=True)
        global num
        num += 1
        print(self.name, '----',num)
        l.release()

    def myTest(self):
        # time.sleep(1)
        time.sleep(random.random())


if __name__ == '__main__':
    # for i in range(10):
    #     me = myThread()
    #     me.start()
    me1 = myThread()
    me2 = myThread()
    me3 = myThread()
    me1.start()
    me2.start()
    me3.start()