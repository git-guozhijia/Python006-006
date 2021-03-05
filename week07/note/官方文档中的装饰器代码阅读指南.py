"""
# 向一个函数添加函数
def attrs(**kwargs):
    def decorate(f):
        for k in kwargs:
            setattr(f, k, kwargs[k])
        return f

    return decorate


@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    pass
print(dir(mymethod))
print(mymethod.author)
"""

"""
import functools

# 函数参数观察器
def trace(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)

    return decorated_function


@trace
def greet(greeting, name):
    return f"{greeting},{name}!"


greet("better", "me")
"""


class MyClass:
    def __init__(self, var_a, var_b):
        self.var_a = var_a
        self.var_b = var_b

    # __eq__ 当判断两个class对象的值是否相等时，触发此方法
    def __eq__(self, other):
        # 判断两个比较的class对象是不是属于一个class
        if self.__class__ is not other.__class__:
            return False
        return (self.var_a, self.var_b) == (other.var_a, other.var_b)


a = MyClass(1, 2)
b = MyClass(1, 2)
c = MyClass(2, 1)

print(a.var_b, a.var_a, a.__class__)

print(a == b)
print(a == c)

# 简化版本
from dataclasses import dataclass


@dataclass
class MyClass:
    var_a: str
    var_b: str


a = MyClass(1, 2)
b = MyClass(1, 2)
# 不用在类中重新封装__eq__
print(a == b)
# 存在缺陷，var_a和var_b不能作为类属性访问
