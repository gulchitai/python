# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Введите натуральное число:'))
col_chet = 0
col_nechet = 0
while True:
    ost = num % 10
    if ost % 2 == 0:
        col_chet +=1
    else:
        col_nechet +=1
    num = num // 10
    if num == 0:
        break

print(f'Количество четных: {col_chet}, количество нечетных: {col_nechet}')
