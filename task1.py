__author__ = 'Куркин Иван'

import collections

c = collections.Counter()
kvartal = 4
count = int(input('Введите количество предприятий: '))
for i in range(count):
    company = input(f'Введите название {i + 1} предприятия: ')
    for j in range(kvartal):
        profit = int(input(f'Введите прибыль {i + 1}-ого предприятия за {j + 1}-й квартал: '))
        c[company] += profit

avr = sum(c.values()) / count

for i in range(len(list(c))):
    if c[list(c)[i]] > avr:
        print(f'Прибыль выше средней у компании {list(c)[i]}')
    elif c[list(c)[i]] < avr:
        print(f'Прибыль ниже средней у компании {list(c)[i]}')
