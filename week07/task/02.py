def my_map(func, iterator):
    for i in iterator:
        yield func(i)


def test_func(value):
    return value ** 2


test_value = my_map(test_func, 1)
for i in test_value:
    print(i)
