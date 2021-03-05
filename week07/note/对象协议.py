class Foo:
    def __str__(self):
        # return "__str__ is called"
        pass

    def __getitem__(self, key):
        print(f"__getitem__ {key}")

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)

    def __iter__(self):
        return iter([i for i in range(5)])
        # pass


bar = Foo()

# print(bar)

bar['key1'] = "value1"
print(bar["key1"])
for i in bar:
    print(i)


# 格式化字符串
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # 直接调用对象的时候会调用__str__
    def __str__(self):
        return f"hello, {self.first_name} {self.last_name}"

    # 对象之间通讯的时候调用__repr__
    def __repr__(self):
        # return f"hello, {self.first_name} {self.last_name}"
        return f"hello, {self.last_name} {self.first_name}"


me = Person("zzh", "zzs")
print(f"{me}")
print(f"{me.__repr__()}")

a = me
print(a)


# 类型注解
# 与鸭子类型相反的是静态类型，声明变量的时候就要置顶类型， 如果使用其他类型对变量赋值就会报错
def func(text: str, number: int) -> str:
    return text * number


print(func('a', 5))
