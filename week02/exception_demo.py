
# 自定义报出异常的类
class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

userinput = 'a'
try:
    if not userinput.isdigit():
        raise UserInputError('用户输入错误')
except UserInputError as err:
    print(err)
finally:
    del userinput

try:
    1/0
except ZeroDivisionError as err:
    print(err)
    try:
        1 / '111'
    except TypeError as err:
        print(err)

# import pretty_errors
# 1 / '111'

# 文件的打开读取
with open('client2.py', encoding='utf-8') as file:
    print(file.readline())
    print(file.readlines())