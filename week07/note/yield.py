def func():
    yield 0


print(type(func))
print(type(func()))

print([i for i in range(0, 11)])  # 列表
print((i for i in range(0, 11)))  # 生成器，生成一个可迭代对象

gen_number = (i for i in range(0, 11))
print(next(gen_number))
print(next(gen_number))
print(next(gen_number))
print(next(gen_number))
print(next(gen_number))
print(list(gen_number))

alist = [1, 2, 3, 4, 5, 6]
# print(dir(alist))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 判断一个对象是否有一个属性
print(hasattr(alist, "__next__"))
print(hasattr(alist, "__iter__"))
# 结论：alist是一个可迭代对象，不是迭代器，因为__next__未实现
for i in alist:
    print(i)

g = (i for i in range(0, 11))
print(hasattr(g, "__next__"))
print(hasattr(g, "__iter__"))
# 结论：alist是一个迭代器，且生成器是实现完整迭代器协议的
print('g.__next__():', g.__next__())
print('g.__next__():', g.__next__())
print('g.__next__():', g.__next__())
print('g.__next__():', g.__next__())
print("next(g):", next(g))
print(list(g))


# 类变成迭代器
class SampleIterator():
    def __iter__(self):
        return self

    def __next__(self):
        # 判断获取的的元素是否是最后一个元素，不是的话返回该元素，是的话直接报出StopIteration异常
        if ...:
            return ...
        else:
            raise StopIteration


# 函数实现完成迭代器协议
def SampleIteratorFunc():
    yield ...
    yield ...
    yield ...


# 只要是函数内定义中出现yield关键字，则此函数变成了一个生成器构造函数，调用此构造函数就可生产一个生成器对象

def check_iterator(obj):
    if hasattr(obj, "__iter__"):
        if hasattr(obj, "__next__"):
            print("迭代器，完成了迭代器协议")
        else:
            print("可迭代对象")
    else:
        print("不可迭代")


def func1():
    yield range(1.11)


check_iterator(func1)
check_iterator(func1())

# 迭代器是使用注意事项
import itertools

# itertools 无线迭代器内常见的三个

count = itertools.count()  # 计数器

print(next(count))
print(next(count))
print(next(count))
print(next(count))

cycle = itertools.cycle((1, 2, '3333', 4))  # 循环遍历
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

repeat = itertools.repeat(10, times=3)  # 重复遍历，限制重复获取的次数
print(next(repeat))
print(next(repeat))
print(next(repeat))

# 有限迭代器
for i in itertools.chain('123', [1, 2, 3]):
    print("有限迭代器itertools.chain()：", i)


def chain(*args):
    for i in args:
        for j in i:
            print(j)
            yield j


s = '123'
t = (11, 22, 33)
print(list(chain(s, t)))


def chain2(*args):
    for i in args:
        print(i)
        yield from i


print(list(chain2(s, t)))

a_dict = {1: 1, 2: 2}
a_dict_iter = iter(a_dict)
print(next(a_dict_iter))
# a_dict[3] = 3
# print(next(a_dict_iter))# RuntimeError: dictionary changed size during iteration
# 一旦转换成迭代器的源字典被改动的话，迭代器被损坏不能被操作了
# 尾插入操作不会损坏指向当前元素的List迭代器，列表自动边长


x = iter([y for y in range(1, 5)])
for i in x:
    i


# print(next(x))  # StopIteration


# yield表达式

def jumping_range(up_to):
    index = 0
    while index < up_to:
        # yield index 为函数的返回值，改行代码后面操作index参数，结果内就会发生变化
        jump = yield index
        print(f"jump is {jump}")
        if jump is None:
            jump = 1
        index += jump
        print(f"index is {index}")


if __name__ == "__main__":
    print("-----------" * 10)
    iterator = jumping_range(5)
    print(list(iterator))
    iterator = jumping_range(5)
    print(next(iterator))  # 调用next()函数，等于启动yield迭代器
    print(iterator.send(2))
    # print(next(iterator))
    # print(next(iterator))
    print(iterator.send(-2))  # 可以将参数值传进yield迭代器内，一定要为非None，如果是None就是和next()是一样的效果
    print(list(iterator))
