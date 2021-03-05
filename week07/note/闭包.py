# version1
# 函数是一个对象，多以可以作为某个函数的返回结果
def line_conf():
    def line(x):
        return 2 * x + 1

    return line


my_line = line_conf()
print(my_line(5))


# version2
def line_conf():
    b = 1

    def line(x):
        return 2 * x + b

    return line


my_line = line_conf()
print(my_line(5))


# version3
def line_conf():
    b = 10

    def line(x):
        return 2 * x + b

    return line


b = -1
my_line = line_conf()
print(my_line(5))

print(my_line.__code__.co_varnames)
print(my_line.__code__.co_freevars)
print(my_line.__closure__[0].cell_contents)


def func():
    a = '111'
    pass


func_magic = dir(func)
print(func_magic)
print(func)


# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


# version4
def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


# 闭包的特性：函数内再次定义函数：外部函数和内部函数不怎么相关，定义态，在定义的是就定义好规则
line1 = line_conf(1, 1)
line2 = line_conf(5, 5)
print(line1(5), line2(5))

# version4
a = 100
b = 200


def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(5, 5)
print(line1(5), line2(5))


def counter(star=0):
    count = [star]

    def incr():
        count[0] += 1
        return count[0]

    return incr


c1 = counter(10)
print(c1())
print(c1())
print(c1())
print(c1())
print(c1())


# nonlocalg关键字标识：可以访问外部函数的局部变量
# 注意start的位置，return的作用域和函数内的作用域不同
def counter2(star=0):
    def incr():
        nonlocal star
        star += 1
        return star

    return incr


c1 = counter(5)
print(c1())
print(c1())
print(c1())
print(c1())
print(c1())
