import queue

q = queue.PriorityQueue()

# 按照优先级取值
q.put((3, "3"))
q.put((11, "11"))
q.put((-12, "-12"))
q.put((2, "2"))
q.put((12, "12"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())


# 后进先出队列
q = queue.LifoQueue()
q.put(111)
q.put(222)
q.put(333)
q.put(444)

print(q.get())
print(q.get())
print(q.get())
print(q.get())

# 还有双向队列
