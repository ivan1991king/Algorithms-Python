__author__ = 'Куркин Иван'

"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). 
Выведите на экран исходный и отсортированный массивы.

"""


import random

def bubble_sort(list1):
    n = 1
    list1_change = True
    while list1_change:
        list1_change = False
        for i in range(len(list1) - n):
            if list1[i] < list1[i + 1]:
                list1[i], list1[i + 1]=list1[i + 1], list1[i]
                list1_change = True
        n += 1

length1 = int(input('Введите количесво элементов в массиве: '))
list1 = [random.randrange(-100, 100) for i in range(length1)]
print(list1)
print()
bubble_sort(list1)
print(list1)
