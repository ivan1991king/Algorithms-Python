__author__ = 'Куркин Иван'

# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100

lst1 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(lst1)

max_x = lst1[0]
max_i = 0
min_x = lst1[0]
min_i = 0
for i in range(1, len(lst1)):
    if lst1[i] > max_x:
        max_x = lst1[i]
        max_i = i
    if lst1[i] < min_x:
        min_x = lst1[i]
        min_i = i
lst1[min_i], lst1[max_i] = max_x, min_x

print(lst1)
