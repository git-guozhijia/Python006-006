# # 参数
# # 可边长参数，非关键字参数和关键字参数是有顺序要求的，非关键字参数是在关键字参数之前的，位置参数是在非关键字参数之前的
# def func(*args, **kwargs):
#     print(args, kwargs)
#
#
# func(123, 1234, 12345, name="kwargs", age=12)


# # lambda
# k = lambda x, y: x * y
# # def k(x, y):
# #     return x * y
# print(k(11, 2))


def square(x):
    return x ** 2


m = map(square, range(10))
# print(list(m))
print("--", next(m))  # 迭代器 把m设置成一个可迭代对象，一个一个的获取值
print(list(m))

print([square(x) for x in range(10)])  # 列表推导式
print(dir(
    m))  # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# reduce()函数
from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [square(x) for x in range(10)]))  # reduce()方法操作，设置一个可迭代对象内的元素依次按照第一个参数（方法对象）进行计算


# filter()函数：过滤作用
def is_old(n):
    return n % 2 == 1


print(list(filter(is_old, [square(x) for x in range(10)])))


# 偏函数：把函数的某一个值固定下来
def add(x, y):
    return x + y


# functools内置模块
import functools

add_1 = functools.partial(add, 1)
print(add_1(10))

# itertools内置模块
import itertools

g = itertools.count()
next(g)
next(g)
next(g)
next(g)
auto_add_1 = functools.partial(next, g)
print(auto_add_1())
