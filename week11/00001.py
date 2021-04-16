import queue

q = queue.Queue()

q.put("1111111")
q.put("1111111")
q.put("1111111")
q.put("1111111")
print(q.qsize())  # 获取队列内的元素个数
print(q.get())
print(q.get())
print(q.get())

# q.task_done()，每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法，以提示q.join()是否停止阻塞，让线程向前执行或者退出；
# q.join()，阻塞，直到queue中的数据均被删除或者处理。为队列中的每一项都调用一次。
q.task_done()

print(q.qsize())  # 获取队列内的元素个数
print(q.empty())  # 判断队列是否为空
print(q.full())  # 判断队列是否满了
# q.join()
