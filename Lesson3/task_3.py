# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

array[max_pos] = min
array[min_pos] = max
print(array)
