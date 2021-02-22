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

    def __getattribute__(self, item):
        print(f"__getattribute__ called item : {item}")
        try:
            return super().__getattribute__(item)
        except AttributeError as err:
            self.__dict__[item] = 100
            return 100


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
# print(h1.age)
# h1.app_print()
h1.app_print()
# print(h1.noater)
# print(h1.__dict__)


