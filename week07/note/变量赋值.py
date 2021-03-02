a = 123
b = 123
c = b

print(id(a))
print(id(b))
print(id(c))

a = 1
b = 2
c = b
c = a = b
print(a, b, c)

x = [1, 2, 3]
y = x
print(x, y)
y.append(4)
print(x, y)

x = [1, 2, 3]
y = [1, 2, 3]
print(id(x[0]))
print(id(y[0]))

a = [4, 5, 6]
b = a
a = [1, 2, 3]
print(a, b)

a = [1, 2, 3]
b = a
a[0], a[1], a[2] = 4, 5, 6
print(a, b)
