class Human(object):
    # 静态字段
    live = True

    # 初始化方法，每次实例化类的时候，都需要按照这个方法实例化
    def __init__(self, name):
        self.name = name


Human.number = 100

# # 添加静态属性
# print(Human.__dict__)
# print(dir(Human))

# # 内置类型不允许增加属性和方法
# # setattr(list, "live", "zzh")  # TypeError: can't set attributes of built-in/extension type 'list'
# setattr(Human, "live", "zzh")
# print(Human.__dict__)

# 显示object类的所有的子类
print(().__class__.__bases__[0].__subclasses__())


class Human01(object):
    _age = 88  # 约定俗成的人为不能修改的属性字段，内部属性，人为修改可能会报错
    # 私有属性，运行代码之后，python会自动给__fly字段修改名字，防止人为去修改这个字段
    # 在类的外部程序去调用该字段的时候，python会自动过滤__标识的字段，外部无法访问
    __fly = False

    # 魔术方法
    def __init__(self):
        self.name = "Human01"
        print(self.__fly)


print(dir(Human01))
a = Human01()
print(a.name)
