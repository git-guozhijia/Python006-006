class Human2():
    def __init__(self):
        self.age = 10

    # 在访问类没有定义的属性的时候，会先访问__getattr__方法，可以去做一些定义，操作
    def __getattr__(self, item):
        print('__getattr__')
        # self.item = item
        # if self.item == "name":
        #     return "__getattr__ self.item = name"
        return "OK"

    # 在访问class属性的时候，都会先访问__getattrbute__方法
    # 由于__getattr__只针对未定义属性的调用，所以它可以在自己的代码中自由地获取其他属性，
    # 而__getattribute__针对所有的属性运行，因此要十分注意避免在访问其他属性时，再次调用自身的递归循环。死循环！！
    # 当在__getattribute__代码块中，再次执行属性的获取操作时，会再次触发__getattribute__方法的调用，代码将会陷入无限递归，直到Python递归深度限制（重载__setter__
    # __setattr__方法也会有这个问题）。
    # 示例代码（无限递归）：
    # def __getattribute__(self, item):
        # self.item = item
        # if self.item == "name":
        #     return "__getattr__ self.item = name"
    # 为了避免无限递归，应该把获取属性的方法 __getattribute__指向一个更高的超类，例如object（因为__getattribute__只在新式类中可用，而新式类所有的类都显式或隐式地继承自object，所以对于新式类来说，object是所有新式类的超类）。利用super（）方法
    def __getattribute__(self, item):
        print("__getattrbute__")
        if item == "name":
            print(f"my name is {item}")
        return super().__getattribute__(item)


# __getattrbute__方法和__getattr__方法同时存在的时候，会先访问__getattribute__方法，在访问__getattr__方法
# __getattrbute__方法存在的时候：访问class属性，不管存在不存在，都会先访问__getattrbute__方法
# __getattr__方法存在的时候：只有访问class不存在的属性才会访问__getattr__方法
h1 = Human2()
# h1.test()
# print(h1.age)
print(h1.name)
print(h1.__dict__)

