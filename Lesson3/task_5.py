# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

size = 20
array = [random.randint(-10,10) for _ in range(size)]

print(array)
index = -1

for i, item in enumerate(array):
    if item < 0 and index == -1:
        index = i
    elif item < 0 and item > array[index]:
        index = i

print(f'Максимальный отрицательный элемент: {array[index]}, находится по индексу {index}')