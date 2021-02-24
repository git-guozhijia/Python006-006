class Humen:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        print(f"__getattribute__ called item : {item}")


class Humen2:
    name = "Humen"

    def __init__(self):
        self.age = 18

    @classmethod
    def app_print(cls):
        print(cls.name)

    # def __getattribute__(self, item):
    #     print(f"__getattribute__ called item : {item}")
    #     try:
    #         return super().__getattribute__(item)
    #     except AttributeError as err:
    #         print(err)
    #         self.__dict__[item] = 100
    #         return 100

    def __getattr__(self, item):
        print("__getattr__",item)


"""
h1 =Humen("zzs")
h2=Humen("zzh")

h1.name = "gzj"

del h1.name

try:
    h1.name
except AttributeError as err:
    print(err)
"""

h1 = Humen2()
h1.app_print()
h1.aaaaa
# print(h1.noater)
# print(h1.__dict__)