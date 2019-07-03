__author__ = 'Куркин Иван'

"""
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
 заданный случайными числами на промежутке [0; 50). 
 Выведите на экран исходный и отсортированный массивы.
"""

import random

def merge_sort(list1):
    if len(list1) > 1:
        middle = len(list1) // 2
        left = list1[:middle]
        right = list1[middle:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1

length1 = int(input('Введите количесво элементов в массиве: '))
list1 = [random.randrange(0, 50) for i in range(length1)]
print(list1)
print()
merge_sort(list1)
print(list1)
