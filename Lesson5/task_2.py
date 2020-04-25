from collections import deque
from collections import  defaultdict

def add_hex(a, b):
    de = deque([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'],16)

    di = defaultdict(list)
    a = a[::-1]
    b = b[::-1]
    for i in range(0,len(a)):
        di[i].append(a[i])

    for i in range(0,len(b)):
        di[i].append(b[i])

    otvet = ''
    dobavka = 0
    for i in di:
        l = di.get(i)
        de_tmp = de.copy()
        index1 = de_tmp.index(l[0])
        index2 = 0
        if len(l) > 1:
            index2 = de_tmp.index(l[1])
        de_tmp.rotate(-1 * (index2+dobavka))

        otvet = otvet + de_tmp[index1]
        dobavka = (index1 + index2) // 15

    if dobavka > 0:
        return str(dobavka) + otvet[::-1]
    else:
        return otvet[::-1]

a = input('Введите первое слагаемое:')
b = input('Введите второе слагаемое:')

print(add_hex(a, b))

