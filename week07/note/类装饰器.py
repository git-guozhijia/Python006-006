"""
from functools import wraps


class myClass:
    def __init__(self, var='init_var', *args, **kwargs):
        self._v = var
        super().__init__(*args, **kwargs)

    def __call__(self, func):
        # 类装饰器
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func_name = func.__name__ + " was called"
            print(*args)
            print(func_name)
            return func(*args, **kwargs)

        return wrapped_function


def myFunc(a, b, c):
    pass


myClass(100)(myFunc)(1,2,3)

"""

"""
# 类作为装饰器
class Count:
    def __init__(self, func):
        self._func = func
        print(func.__name__)
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"num of call is {self.num_calls}")
        return self._func(*args, **kwargs)

# class作为装饰器，想要实现语法糖，需要编写class装饰器内的__call__()函数，才可以使用这个语法
@Count
def example():
    print("hellow example")


example()
example()
example()
example()
"""


# 装饰器装饰类：装饰器函数内编写class，装饰类
def decorator(aClass):
    class newClass():
        def __init__(self, args):
            self.times = 0
            # 被装饰的类实例的引用为self.wrapped
            self.wrapped = aClass(args)

        def display(self):
            self.times += 1
            print(f"run times {self.times}")
            self.wrapped.display()

        # def myName(self):
        #     print("my name is newClass.MyName")

    return newClass

# 被类装饰器装饰之后，被装饰的类内函数，如果没有在装饰器内重写的话，在外部调用的时候会报错，因为在装饰器内未找到
@decorator
class MyClass():
    def __init__(self, number):
        self.number = number

    def display(self):
        print(f"number is {self.number}")

    def myName(self):
        print(f"my name is MyClass.myName")


six = MyClass(6)

for i in range(5):
    six.display()
    six.myName()


