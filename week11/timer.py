from threading import Timer

n = 0


def hello():
    global n
    n += 1
    print(n)


for i in range(10):
    t = Timer(1, hello)
    t.start()
