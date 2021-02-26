class Displayer(object):
    def display(self, message):
        print("Displayer display")
        print(message)


class LogerMixin(object):
    def log(self, message, filename="logfile.txt"):
        print("LogerMixin log function")
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        print("LogerMixin display")
        # super(LogerMixin, self).display(message) # 等同于super().display(message)，这是python2的写法
        super().display(message)
        self.log(message)


class MySubClass(LogerMixin, Displayer):
    def log(self, message):
        super().log(message, filename="subclasslog.txt")


mysubclass = MySubClass()
print(MySubClass.mro())
# mysubclass.log("mysubclass log")
mysubclass.display("mysubclass.display")
