# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random
size = 11
array = [random.randint(0,50) for i in range(size)]

print(array)

for i in range(len(array)):
    n = 0
    m = 0
    for j in range(len(array)):
        if array[j] != array[i]:
            if array[j] > array[i]:
                n += 1
            else:
                m += 1
    if n == m:
        print(f'{array[i]} - медиана')
        break

print(sorted(array))


