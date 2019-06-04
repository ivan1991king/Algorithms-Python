__author__ = 'Куркин Иван'

# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

lst1 = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(SIZE)]
print(lst1)
min_d = -100
min_i = 0

for i in range(0, len(lst1)):
    if min_d < lst1[i] < 0:
        min_d = lst1[i]
        min_i = i

print(f"Максимальный отрицательный элемент в списке: {min_d}, его индекс {min_i}")
