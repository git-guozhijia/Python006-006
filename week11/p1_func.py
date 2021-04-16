import threading,os

def run(n):
	print(f"current  task {n} , 当前进程ID:{os.getpid()}")


class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, name):
		super(MyThread, self).__init__()
		self.name = name

	def run(self):
		print(f"current  task {self.name}, 当前进程ID:{os.getpid()}")
		


if __name__ == '__main__':
	t1 = threading.Thread(target=run, args=("多线程t1",))
	t2 = threading.Thread(target=run, args=("多线程t2",))

	print(f"t1.is_alive(): {t1.is_alive()}")
	t1.start()
	t2.start()
	print(f"t1.is_alive(): {t1.is_alive()}")# 判断线程是否存活
	print(f"t1.getName()：{t1.getName()}")# 获取当前线程的名称
	print(f"t2.getName()：{t2.getName()}")
	t1.join()
	t2.join()
	print(f"t1.is_alive(): {t1.is_alive()}")


	t3 = MyThread("thread 01")
	t4 = MyThread("thread 02")

	t3.start()
	t4.start()
	print(f"t3.getName()：{t3.getName()}")
	print(f"t4.getName()：{t4.getName()}")
	t3.join()
	t4.join()

	# 调用方
	# 阻塞，得到调用结果之前，线程会被挂起
	# 非阻塞，不能理解得到结果，不会阻塞线程

	# 被调用方
	# 同步 得到结果之前，调用不会返回
	# 异步 请求发出后，调用立即返回，没有返回结果，通过回调函数获得实际结果