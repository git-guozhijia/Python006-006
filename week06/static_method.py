import datetime


class Story(object):
    snake = "python"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def god_come_gp():
        if datetime.datetime.now().month % 2:
            print("god is coming")


Story.god_come_gp()


class Foo:
    def instance_method(self):
        print("是类的实例方法，只能被对象调用")

    @classmethod
    def class_method(cls):
        print("classmethod function")

    @staticmethod
    def static_method():
        print("staticmethod function")


foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print("*" * 50)
Foo.static_method()
Foo.class_method()
# Foo.instance_method()
