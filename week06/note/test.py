from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concrete(Base):
    def foo(self):
        pass

    def bar(self):
        pass


if __name__ == "__main__":
    pass
    # 当只去实现Concrete继承自Base类的一个抽象方法时，另一个抽象方法不实现就会报错
    c = Concrete()  # TypeError: Can't instantiate abstract class Concrete with abstract method bar

    # TypeError: Can't instantiate abstract class Base with abstract methods bar, foo
    # b = Base() # 抽象基类不能去实例化
