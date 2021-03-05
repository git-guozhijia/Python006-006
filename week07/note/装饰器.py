# 装饰器
def decorate(func):
    print("running in modlue")

    def inner():
        print(1111111111)
        return func()

    return inner


@decorate
def func2():
    print(1111)


'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "flask index func!"


if __name__ == "__main__":
    app.run(debug=True)
'''


# 被装饰函数带定长参数和返回值的处理

def outer(func):
    def inner(a, b):
        print(func.__name__)
        print(a, b)
        func(a, b)

    return inner


@outer
def foo(a, b):
    print(a + b)
    print('-----------', foo.__name__)


foo(1, 2)


# 被装饰函数带不定长参数和返回值的处理
def outer2(func):
    def inner2(*args, **kwargs):
        print(args, kwargs)
        func(*args, **kwargs)

    return inner2


@outer2
def foo2(a, b, c):
    print(a + b + c)


foo2(1, 3, 5)


# 被装饰的函数带有返回值
def outer3(func):
    def inner3(*args, **kwargs):
        print(args, kwargs)
        ret = func(*args, **kwargs)
        return ret

    return inner3


@outer3
def foo3(a, b, c):
    return a + b + c


print(foo3(1, 3, 5))


# 装饰器带参数
def outer_arg(bar):
    def outer(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(bar)
            return ret

        return inner

    return outer


# 等同于outer_arg('gzj')(foo)(a, b, c)
@outer_arg("gzj")
def foo(a, b, c):
    return (a + b + c)


print(foo(1, 2, 3))


# # 装饰器的堆叠，多个装饰器叠放在一起
# @classmethod
# @synchronized
# def foo(cls):
#     pass
# foo2 = synchronized(lock)(foo)
# foo = classmethod(foo2)
