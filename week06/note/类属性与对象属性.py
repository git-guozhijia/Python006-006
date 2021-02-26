class Human(object):
    # 静态字段
    live = True

    # 初始化方法，每次实例化类的时候，都需要按照这个方法实例化
    def __init__(self, name):
        self.name = name


man = Human('zzs')
woman = Human('zzh')

# 有静态字段，live属性
print(Human.__dict__)
# 有普通字段，name属性
man.live = False
print(man.__dict__)  # 可以获取到live静态字段，在上面设置了man.live字段
print(woman.__dict__)  # 不可以获取到live静态字段

print(Human.live)
print(man.live)
print(woman.live)


class MyFirstClass:
    pass


a = MyFirstClass()
b = MyFirstClass()

print(a.__class__())
print(b.__class__())
print(id(a))
print(id(b))

c = MyFirstClass()

print(type(c))
d = c
print(d.__class__())
