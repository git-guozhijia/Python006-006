# 布尔运算 --- and, or, not
print(111) if 1 or 2 else print(222)
print(111) if 1 and 2 else print(222)
print(111) if not 1 else print(222)

# 111
# 111
# 222

# 比较运算
print("对") if 1 > 2 else print("错")
print("对") if 1 < 2 else print("错")
print("对") if 1 >= 2 else print("错")
print("对") if 1 >= 2 else print("错")
print("对") if 1 == 2 else print("错")
print("对") if 1 != 2 else print("错")
print("对") if 1 is 1 else print("错")# 对象标识  is 和 is not 运算符无法自定义；并且它们可以被应用于任意两个对象而不会引发异常。
print("对") if 1 is not 1 else print("错")# 否定的对象标识
# 错
# 对
# 错
# 错
# 错
# 对
# 对
# 错
a = 1
b = 1
c = 2
print("对") if a is c else print("错")
print("对") if a is not c else print("错")
print("对") if a is b else print("错")
# 错
# 对
# 对

# 数字类型 --- int, float, complex
print( 1+3 )
print( 1-3 )
print( 1*3 )
print( 1/3 )
print( 7//3 )
print( 7%3 )