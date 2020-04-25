# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import defaultdict
import statistics

my_list = []
while True:
    org, profit = input("Введите организацию и прибыль через пробел (0 - конец ввода): ").split()
    if org == '0':
        break
    l = []
    l.append(org)
    l.append(int(profit))
    my_list.append(l)

print(my_list)

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)


d1 = defaultdict(int)
for i in d:
    sum1 = sum(d[i].copy())
    d1[i] = sum1
print(d1)

avg_org = statistics.mean(d1.values())
print(avg_org)
for i in d1:
    if d1[i] > avg_org:
        print(f'В организации "{i}" прибыль выше среднего')
    else:
        print(f'В организации "{i}" прибыль ниже или равна средней')