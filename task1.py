__author__ = 'Куркин Иван'
"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в 
рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным
 использованием памяти. Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет: 
 ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти; 
 ● написать 3 варианта кода (один у вас уже есть); ● проанализировать 3 варианта и выбрать оптимальный; 
 ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. 
 Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python; 
 ● написать общий вывод: какой из трёх вариантов лучше и почему.
  Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, 
а проявили творчество, фантазию и создали универсальный код для замера памяти.
"""

import random
import sys

# Функция для подсчета объема занятой памяти

def calc_size(x):
    sum_key = 0
    sum_value = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                sum_key = sum_key + sys.getsizeof(key)
                print(f'type = {type(key)}, size = {sys.getsizeof(key)}, object = {key}')
                sum_value = sum_value + sys.getsizeof(value)
                print(f'type = {type(value)}, size = {sys.getsizeof(value)}, object = {value}')
            print(f'Память, занятая ссылками на переменные = {sum_key}')
            print(f'Память, занятая значениями переменных = {sum_value}')
    print(f'Память, занятая функцией = {sys.getsizeof(x)}')
    print(f'Всего занято памяти: {sys.getsizeof(x) + sum_key + sum_value}')


# 3 задача 3 урока
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def change_places():
    length = 10
    lst = [random.randint(0, 100) for i in range(length)]
    print(lst)
    min_d = lst[0]
    max_d = lst[0]
    min_i = 0
    max_i = 0

    for i in range(1, len(lst)):
        if lst[i] > max_d:
            max_d = lst[i]
            max_i = i
        if lst[i] < min_d:
            min_d = lst[i]
            min_i = i

    lst[max_i], lst[min_i] = lst[min_i], lst[max_i]
    print(lst)
    return vars()

print()
calc_size(change_places())

# Память, занятая ссылками на переменные = 205
# Память, занятая значениями переменных = 184
# Память, занятая функцией = 204
# Всего занято памяти: 593




# 4 задача 3 урока
#Определить, какое число в массиве встречается чаще всего
def find_count():
    length=20
    lst=[random.randint(0, 10) for i in range(length)]

    count=0
    max_count=0
    num=0

    for i in range(len(lst) - 1):
        if lst[i] != num:
            for j in range(i + 1, len(lst)):
                if lst[i] == lst[j]:
                    count+=1
            if count > max_count:
                max_count=count
                num=lst[i]
            count=0

    if num == 0:
        print(lst)
        print('В массиве нет повторяющихся чисел')
    else:
        print(lst)
        print(f'Число {num} встречается в массиве чаще всего, {max_count + 1} раз(а)')
    return vars()

print()
calc_size(find_count())

# Память, занятая ссылками на переменные = 203
# Память, занятая значениями переменных = 218
# Память, занятая функцией = 204
# Всего занято памяти: 625

#Windows 7, 64-разрядная ОС, Python 3.7
#Чем больше переменных, тем больше памяти занимает
#Ссылки занимают больше памяти, чем сами значения, если это не списки.
#Списки очень тяжелые
