from multiprocessing import Queue, Process
import time


def write(q):
    for i in ["a", "b", "c", "d"]:
        q.put(i)
        print(f"put {i} to queue")


def read(q):
    print(f"get {q.get()} from queue")
    while 1:
        print(f"get {q.get()} from queue")


def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    # pr = Process(target=read,args=(q,))
    pw.start()
    # time.sleep(3)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    # print(q.get())
    # pr.start()
    pw.join()
    # time.sleep(3)
    # pr.terminate()


if __name__ == "__main__":
    main()
