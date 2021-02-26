class Human(object):
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender


class Woman(Human):
    def __init__(self, name):
        self.name = name
        print(f"Woman __init__ name : {self.name}")


class Man(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print(f"Woman __init__ name : {self.name}")


class Factory:
    def getPerson(self, name, gender):
        if gender == "m":
            return Man(name)
        elif gender == "f":
            return Woman(name)
        else:
            pass


# 返回在函数内动态创建的类
def factory2(func):
    class klass: pass

    # 为空类添加方法
    setattr(klass, func.__name__, classmethod(func))
    # setattr(klass, func.__name__, func)
    return klass


def say_foo(self):
    print(1111)


if __name__ == "__main__":
    # # 简单工厂模式
    # f = Factory()
    # a = f.getPerson("sss", "m")
    # print(a.getName())
    # print(a.getGender())

    Foo = factory2(say_foo)
    foo = Foo()
    foo.say_foo()
    Foo = factory2(say_foo)
    Foo().say_foo()