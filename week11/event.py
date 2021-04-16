import threading, time

num = 0


def func(e):
    # print(f"第{i+1}运行func()方法！")
    e.wait()
    time.sleep(1)
    global num
    num += 1
    print(f"num : {num}")


# 事件：定义一个flag，set()函数设置flag=True，clear()函数设置flag为False
event = threading.Event()
for i in range(10):
    t = threading.Thread(target=func, args=(event,))
    t.start()

event.clear()

for i in range(100):
    if i == 30:
        print(f"for i in range(100) ：{i}")
        event.set()
