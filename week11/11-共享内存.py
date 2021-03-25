from multiprocessing import Process, Value, Array, Queue


def f(n, a):
    n.value = 3.1514927
    for i in a:
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value("d", 0.0)
    arr = Array("i", range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
