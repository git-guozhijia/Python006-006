class Kls1(object):
    bar = 1

    def __init__(self):
        self.name = "Kls1"

    # @classmethod 装饰之后，可以在类外部调用的时候不用类的实例化对象去调用，直接类名调用即可
    def foo(slef):
        print(slef.name)

    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__dict__)
        print(cls.__name__)
        cls().foo()

    @staticmethod
    def class_foo01():
        print("@staticmethod 装饰器")


"""
Kls1.class_foo()
# Kls1.foo()
kls1 = Kls1()
kls1.class_foo()

Kls1.class_foo01()
kls1.class_foo01()
"""


class Story(object):
    snaka = "python"

    # 初始化函数
    def __init__(self, name):
        self.name = name

    # # 构造函数
    # def __new__(cls, *args, **kwargs):
    #     pass

    @classmethod
    def get_apple_to_eve(cls):
        return cls.snaka


"""
s = Story("zzh")
print(s.__dict__)
print(Story.__dict__)
print(Story.get_apple_to_eve)
print(Story.get_apple_to_eve())  # 被@classmethod装饰器装饰的函数，可以在外部直接跳过初始化函数直接调用
# 使用类的实例化去调用get_apple_to_eve()方法的时候，会先去自身的__dict__内查找是否有get_apple_to_eve()方法，如果没有回去Story.__dict__内查找该方法
print(s.get_apple_to_eve())  # 被@classmethod装饰器装饰的函数，也可以在类的实例化下调用
print(s.name)
print(s.snaka)
"""


class Kls2(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f"first name is {self.fname}")
        print(f"last name is {self.lname}")


class Kls3(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def pre_name(cls, name):
        fname, lname = name.split("-")
        return cls(fname, lname)

    def print_name(self):
        print(f"first name is {self.fname}")
        print(f"last name is {self.lname}")

class Kls4(object):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def pre_name(cls, name):
        fname, lname = name.split(",")
        return cls(fname, lname)

    def print_name(self):
        print(f"first name is {self.fname}")
        print(f"last name is {self.lname}")

"""
me = Kls2("win10", "mac")
me.print_name()

# me = Kls2("zzh-zzs")  # TypeError: __init__() missing 1 required positional argument: 'lname'
me = Kls3.pre_name("zzh-zzs")
me.print_name()


me = Kls4.pre_name("zzh,zzs")
me.print_name()
"""

class Fruit(object):
    total = 0
    @classmethod
    def print_totle(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))
    @classmethod
    def set(cls, value):
        print(f"calling {cls.__name__} {value}.")
        cls.total = value

class Apple(Fruit):
    pass
class Orange(Fruit):
    pass

Apple.set(100)
Orange.set(200)
org = Orange()
org.set(500)

Orange.print_totle()
Apple.print_totle()
Fruit.print_totle()
