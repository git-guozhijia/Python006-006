# from functools import partial

"""
# 实现方式：
返回一个新的 部分对象，当被调用时其行为类似于 func 附带位置参数 args 和关键字参数 keywords 被调用。 如果为调用提供了更多的参数，它们会被附加到 args。 如果提供了额外的关键字参数，它们会扩展并重载 keywords。 大致等价于:

def partial(func, /, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

partial() 会被“冻结了”一部分函数参数和/或关键字的部分函数应用所使用，从而得到一个具有简化签名的新对象。 例如，partial() 可用来创建一个行为类似于 int() 函数的可调用对象，其中 base 参数默认为2

"""


def partial(func, /, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        print(args, keywords)
        print(fargs, fkeywords)
        print(f"func(*args:{args}, *fargs:{fargs}, **newkeywords:{newkeywords})")
        return func(*args, *fargs, **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))# int('10010', base=2)

"""
注意点：
1，partial 第一个参数必须是可调用对象
2，参数传递顺序是从左到右的，但不能超过原函数参数个数
3，关键字参数不会覆盖partial中定义好的参数
"""
