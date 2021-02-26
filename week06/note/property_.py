# property 属性描述符


class Desc:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        print(f"__get__{instance},{owner}")
        return self.name

    def __set__(self, instance, value):
        print(f"__set__{instance},{value}")
        self.name = value

    def __delete__(self, instance):
        print(f"__delete__ {instance}")
        del self.name


class MyObj:
    a = Desc('aaa')
    b = Desc('bbb')


# my_obj = MyObj()
# my_obj.a = 555
# print(my_obj.a)


class Human:
    def __init__(self, nmae):
        self.name = nmae
        self._gender = None

    # @property装饰器，可以将class的方法封装成class的属性
    # 被装饰之后，只能去读，不能去写或者修改
    @property
    def gender(self):
        return self.name

    # 设置支持修改和删除的方法，使用property封装成属性
    @property
    def gender2(self):
        print(self._gender)

    @gender2.setter
    def gender2(self, value):
        print("@gender2.setter gender2 value")
        self._gender = value

    @gender2.deleter
    def gender2(self):
        del self._gender


h1 = Human("zzh")
print(h1.gender)
# h1.gender = "f"# AttributeError: can't set attribute
h1.gender2 = "name"
h1.gender2

'''
被装饰函数建议使用相同的gender2
使用setter 并不能真正意义上时间无法写入，gender被改名为_Articel_gender

property本质并不是函数，而是特殊类（实现了数据描述符的类）
如果一个对象同时定义了__get__()和__set__()方法，则被称为数据描述符
如果仅定义了__get__（）方法，则被称为非数据描述符

property的有点：
1，代码更简洁，可读性，可维护性更高
2，更好的管理属性的访问
3，控制属性访问权限，提高数据安全性
'''


class Age:
    def __init__(self, default_age=18):
        self.age_range = range(18, 99)
        self.default_age = default_age
        self.data = {}

    def __get__(self, instance, owner):
        # # 使用字典的get方法获取字典内的键值对，如果获取的值没有值的话，赋予一个值
        # data = {"aaa": '111'}
        # print(data.get('aaaa', '2222'))
        return self.data.get(instance, self.default_age)

    def __set__(self, instance, value):
        if value not in self.age_range:
            raise ValueError("must be in (18-99)")
        self.data[instance] = value


class Student():
    age = Age()


if __name__ == "__main__":
    s1 = Student()
    a1 = Age()
    print(s1.age)
    s1.age = 90
    print(s1.age)
    # s1.age = 900 # 执行报错，报错原因为ValueError: must be in (18-99)


