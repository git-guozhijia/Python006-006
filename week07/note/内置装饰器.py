'''
# 内置装饰器函数

from time import ctime, sleep
from functools import wraps


def outer_arg(bar):
    def outer(func):
        # @wraps(func)
        def inner(*args, **kwargs):
            print(f"{func.__name__} called at {ctime()}")
            ret = func(*args, **kwargs)
            print(bar)
            return f"----{ret}"

        return inner

    return outer


@outer_arg("gzj")
def foo(a, b, c):
    return (a + b + c)


print(foo(1, 2, 3))
print(foo.__name__)


# wraps()内置函数
from functools import wraps


def logit(logfile="out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " war called"
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myFunc00():
    pass


myFunc00()
print(myFunc00.__name__)


@logit(logfile="out.log")
def myFunc01():
    pass


myFunc01()
print(myFunc00.__name__)
'''
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    # print(fibonacci(n - 2) + fibonacci(n - 1))
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))
