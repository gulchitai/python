# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# Выбрала задание 4 с урока 2.
# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

# col = int(input('Введите количество элементов ряда:'))
# num = 1
# sum = 0
# for i in range(col):
#     sum = sum + num
#     num = -1 * num / 2
# print(f'Сумма элементов ряда:{sum}')

import functools
import cProfile

#####################################################################
# первый вариант реализованного мной алгоритма оформлю в виде функции
def sum_number_series_loop(n):
    num = 1
    sum = 0
    for i in range(n):
        sum = sum + num
        num = -1 * num / 2
    return sum

#"task_1.sum_number_series_loop(10)"
#1000 loops, best of 5: 2.34 usec per loop

#"task_1.sum_number_series_loop(100)"
#1000 loops, best of 5: 17.8 usec per loop

#"task_1.sum_number_series_loop(400)"
#1000 loops, best of 5: 72.7 usec per loop

########################################################################
#второй вариант будет с использованием рекурсии
def sum_number_series(n):
    if n == 1:
        return 1, 1
    sum_prev, num = sum_number_series(n-1)
    num = -1 * num / 2
    return sum_prev + num, num

#"task_1.sum_number_series(10)"
#1000 loops, best of 5: 3.89 usec per loop

#"task_1.sum_number_series(100)"
#1000 loops, best of 5: 41.3 usec per loop

#"task_1.sum_number_series(400)"
#1000 loops, best of 5: 182 usec per loop

cProfile.run('sum_number_series(400)')

#######################################################################
#третий вариант с меморизацией "из коробки"
@functools.lru_cache()
def sum_number_series_cache(n):
    if n == 1:
        return 1, 1
    sum_prev, num = sum_number_series(n-1)
    num = -1 * num / 2
    return sum_prev + num, num

#"task_1.sum_number_series_cache(10)"
#1000 loops, best of 5: 146 nsec per loop

#"task_1.sum_number_series_cache(100)"
#1000 loops, best of 5: 154 nsec per loop

#"task_1.sum_number_series_cache(400)"
#1000 loops, best of 5: 150 nsec per loop

#cProfile.run('sum_number_series_cache(400)')

# n = 500
# print(sum_number_series_loop(n))
# print(sum_number_series(n)[0])
# print(sum_number_series_cache(n)[0])

#########################################################################
########### ВЫВОД #######################################################
#########################################################################
#Вывод: третий алгоритм - рекурсия с меморизацией "из коробки" работает быстрее всего за счет кеширования
# (запоминания результатов выполнения функции с разными аргументами), минус в том, что при больших значениях n
# выдает ошибку "максимальная глубина рекурсии превышена"
