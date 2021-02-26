'''
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

复制代码
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
具体要求：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

'''
from abc import ABCMeta


class Animal(metaclass=ABCMeta):
    def __init__(self, animalType, shape, character):
        self.animalType = animalType
        self.character = character

        if shape == "低等":
            self.shape = 1
        elif shape == "中等":
            self.shape = 2
        elif shape == "高等":
            self.shape = 3
        else:
            raise ValueError("shape参数输入错误")

    @property
    def isFerociousAnimal(self):
        if self.animalType == "食肉类型" and self.shape >= 2 and self.character == "性格凶猛":
            return True
        else:
            return False


class Cat(Animal):
    def __init__(self, animalType, shape, character, name):
        self.name = name
        super().__init__(animalType, shape, character)
        self.isSuitableToPet = self.isFerociousAnimal

    @property
    def Calls(self):
        return "喵喵喵"


class Dog(Animal):
    def __init__(self, animalType, shape, character, name):
        self.name = name
        super().__init__(animalType, shape, character)
        self.isSuitableToPet = self.isFerociousAnimal

    @property
    def Calls(self):
        return "旺旺旺"


class Zoo():
    def __init__(self, name):
        self.name = name

    def add_animal(self, animal):
        if hasattr(self, animal.__class__.__name__):
            print(f"{animal.__class__.__name__} 已经被创建过，请勿重复添加")
        else:
            setattr(self, animal.__class__.__name__, animal)


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    # cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat1 = Cat(animalType="食肉类型", shape="低等", character="性格凶猛", name="zzh")

    have_cat = hasattr(z, 'Cat')
    print(have_cat)

    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
    print(z.__dict__)
