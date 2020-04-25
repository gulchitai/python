# 4. Определить, какое число в массиве встречается чаще всего.

import random

size = 20
array = [random.randint(1,10) for _ in range(size)]

print(array)
d ={}
for i in array:
    if d.get(i, 0) == 0:
        d[i] = 1
    else:
        d[i] = d[i] + 1

max_value = 1
max_key = 0
for i, item in enumerate(d):
    if max_value < d[item]:
        max_value = d[item]
        max_key = item
print(d)
print(f'Число {max_key} встречается в массиве {max_value} раз')
