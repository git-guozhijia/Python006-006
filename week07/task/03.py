# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time
from functools import wraps
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='test.log',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='[%(asctime)s]-%(levelname)s-%(message)s')


def timer(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        logging.info(f"{func.__name__}函数运行时间：{start - end}")
        print(f"{func.__name__}函数运行时间：{start - end}")
        return start - end

    return inner_func


@timer
def test_time(name1, name2, name3):
    time.sleep(name1)
    time.sleep(name2)
    time.sleep(name3)


test_time(1, 2, 3)
