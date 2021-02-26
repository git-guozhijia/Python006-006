class People:
    def __init__(self):
        self.gene = "XY"
        self.name = "Peopel"

    def walk(self):
        print("I can walk")


class Man(People):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def work(self):
        print('work hard')


class Woman(Man):
    # def __init__(self, name):
    #     self.name = name

    def shopping(self):
        print("buy buy buy")

class chile(Woman, Man, People):
    pass

p = People()
print(p.__dict__)
m = Man("zzh")
print(m.name)
print(m.__dict__)
w = Woman("aaaa")
print(w.work())
print(w.walk())
print(Woman.mro())

# 使用mro可以获取class的继承顺序
c = chile("aaa")
print(chile.mro())
