__author__ = 'Куркин Иван'

"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, 
делящий его на две равные части: в одной находятся элементы, 
которые не меньше медианы, в другой — не больше медианы.
"""
import random

def find_mediana(list1):
    part1 = []
    list2 = list1[:]
    i = 0

    while i <= (len(list1) // 2):
        min_d = min(list2)
        part1.append(min_d)
        list2.pop(list2.index(min_d))
        i += 1
    print(part1[-1])

length1 = (2 * random.randint(5, 10)) + 1
list1 = [random.randrange(0, 50) for i in range(length1)]
print(list1)
print()
find_mediana(list1)
