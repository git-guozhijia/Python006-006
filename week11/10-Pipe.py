from multiprocessing import Process, Pipe


def run(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    # Pipe()函数默认返回一个管道的连接对象，默认情况下双向的
    # 返回的parent_conn，child_conn两个对象，表示管道的两端，每个链接对象都有send()和recv()方法
    # 请注意：如果多个线程（或者进程），同时尝试向管道内的同一端写入或者读取数据，有可能造成数据损坏，同时使用管道的不同端，不会损坏数据
    parent_conn, child_conn = Pipe()
    p = Process(target=run, args=(parent_conn,))
    p.start()
    print(child_conn.recv())
    p.join()
