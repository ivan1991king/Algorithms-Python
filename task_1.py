__author__ = 'Куркин Иван'

# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# Решение 1
for x in range(2, 10):
    count = 0
    for y in range(2,100):
        if y % x == 0:
            count += 1
    print(f'Числу {x} кратно {count} чисел из диапазона от 2 до 99')

# Решение 2 через словарь
spisok = {}
for x in range(2, 100):
    for y in range(2, 10):
        if x % y == 0:
            if y in spisok:
                spisok[y] += 1
            else:
                spisok[y] = 1
print(spisok)
