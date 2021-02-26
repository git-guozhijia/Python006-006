"""
def singleton(cls):
    instance = {}
    def getinstance():
        if cls not in instance:
            instance[cls] = cls()
            print(instance)
        print(instance)
        return instance[cls]
    return getinstance

@singleton
class testClass(object):
    pass

class01 = testClass()
class02 = testClass()

print(id(class01))
print(id(class02))
"""

"""

# 单例模式，只能被创建一次的类，仅限于单线程使用，多线程需要添加线程锁
class Singleton2(object):
    __isinstance = False
    def __new__(cls, *args, **kwargs):# cls 代表的是Singleon类本身，即self
        # print(cls)
        if cls.__isinstance:
            print(1)
            return cls.__isinstance
        print(2)
        cls.__isinstance = object.__new__(cls)# cls 代表的是Singleon类本身
        return cls.__isinstance
    def __init__(self, name):
        self.name = name
        print(self.name)

s = Singleton2("sadasd")
s2 = Singleton2("sadasd")
s3 = Singleton2("sadasd")
"""


import threading
class Singleton2(object):
    objs = {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.objs[cls]
        cls.objs_locker.acquire()
        try:
            if cls in cls.objs:
                return cls.objs
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()