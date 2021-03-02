old_list = [i for i in range(1, 11)]
new_list = old_list
new_list2 = list(old_list)

print(id(old_list))
print(id(new_list2))
print(id(new_list))
"""
4473501248
4473963776
4473501248
"""

new_list3 = old_list[:]
print(id(new_list3))

old_list.append([11, 12])
print(id(old_list))
print(new_list3)
print(new_list2)
print(new_list)

import copy

new_list4 = copy.copy(old_list)
new_list5 = copy.deepcopy(old_list)
# print(id(new_list5))
# print(id(new_list4))
# print(id(old_list))
print(id(new_list5[-1]))
print(id(new_list4[-1]))
print(id(old_list[-1]))

# collections

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
x, y = Point(y=1, x=3)

print(x)
print(y)

from collections import Counter

list01 = [1, 2, 3, 4, 45, 6, 7, 543, 22, 3423, 3, 4, 4, 53, 3, 3, 3, 33]
print(Counter(list01).most_common(3))

from collections import deque

d = deque('a')
d.append('b')
print(d)
d.appendleft('c')
print(d)


