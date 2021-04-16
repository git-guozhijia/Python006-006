import threading


def condition():
    ret = False
    r = input(">>>")
    if r == "yes":
        ret = True
    return ret


def func(conn, i):
    conn.acquire()
    conn.wait_for(condition)
    print(i + 100)
    conn.release()


c = threading.Condition()

# 条件锁，该机制会线程等待，只有满足某条件时，才能释放n个线程
c = threading.Condition()
for i in range(2):
    t = threading.Thread(target=func, args=(c, i,))
    t.start()
