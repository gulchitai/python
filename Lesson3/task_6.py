# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

size = 10
array = [random.randint(1,100) for _ in range(size)]

print(array)
min = max = array[0]
min_pos = max_pos = 0

for i in range(1, size):
    if min > array[i]:
        min = array[i]
        min_pos = i
    if max < array[i]:
        max = array[i]
        max_pos = i
print(f'min={min}, max={max}')
print(f'min_pos={min_pos}, max_pos={max_pos}')
sum = 0
for i in range(size):
    if (min_pos < max_pos and i > min_pos and i < max_pos) or (max_pos < min_pos and i < min_pos and i > max_pos):
        sum +=array[i]

print(sum)
