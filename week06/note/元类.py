class Apple(object):
    pass


print(type(Apple))


def hi():
    print("my name is hi!")


# type 的参数：类名，父类元祖，类的成员
foo = type("Foo", (), {"say_hi": hi})
print(type(foo))
print(foo.__dict__)
foo.say_hi()


def pop_value(self, dict_value):
    for key in self.keys():
        # print(key)
        # print(self.__getitem__(key))
        if self.__getitem__(key) == dict_value:
            self.pop(key)
            break


class DelValue(type):
    # 元类：编写元类必须重写__new__方法，必须要继承type，不能是object
    def __new__(cls, name, bases, attrs):
        """
        # 元类编写__new__方法，name，bases，attrs三个参数必填
        :param name: 名字
        :param bases: 父类
        :param attrs: 属性
        """
        # attrs 添加的属性，就是DelValue class的属性
        attrs['pop_value'] = pop_value
        return type.__new__(cls, name, bases, attrs)


class DelDictValue(dict, metaclass=DelValue):
    pass

# d = DelDictValue()
#       d = DelDictValue() = DelValue + dict  相当于d就是一个字典+DelValue的一个混合类。pop_value方法内的self相当于是d本身，也就是个字典    d.pop_value(d, "c")  相当于是调用本身类的一个方法

d = DelDictValue()
d["a"] = "A"
d["b"] = "B"
d["c"] = "C"
# print(d)
d.pop_value("C")
print(d)
