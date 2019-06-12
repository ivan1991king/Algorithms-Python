__author__='Куркин Иван'

# за базу взял первую задачу из дз к 3 уроку.
# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Задачу модернизировал, теперь эта функция которая возвращает кол-во чисел в диапазоне 100**2 (для усложнения
# вычисление) кратному аргументу функции.

import timeit
import cProfile


# Решение 1

def spisok(n):
    count = 0
    for y in range(2, 100**2+1):
        if y % n == 0:
            count += 1
    return count

# >python -m timeit -n 100 -s "import task1" "task1.spisok(7)"
# 100 loops, best of 5: 1.13 msec per loop
#       1    0.002    0.002    0.002    0.002 task1.py:14(spisok)


# Решение 2 через словарь

def spisok2(n):
    spisok={}
    for x in range(2, 100**2+1):
            if x % n == 0:
                if n in spisok:
                    spisok[n]+=1
                else:
                    spisok[n]=1
    return spisok[n]

# >python -m timeit -n 100 -s "import task1" "task1.spisok2(7)"
# 100 loops, best of 5: 1.38 msec per loop
#     1    0.002    0.002    0.002    0.002 task1.py:28(spisok2)

# Решение 3 нелогичное для сравнения через списки

def spisok3(n):
    lst1 = [i for i in range(2, 100**2 + 1)]
    lst2 = [i for i in range(2, 10)]
    count = [0] * len(lst2)
    for i in range(len(lst2)):
        for j in range(len(lst1)):
            if lst1[j] % lst2[i] == 0:
                count[i]+=1
        if lst2[i] == n:
            return count[i]

# >python -m timeit -n 100 -s "import task1" "task1.spisok3(7)"
# 100 loops, best of 5: 14.6 msec per loop
#    1    0.023    0.023    0.024    0.024 task1.py:44(spisok3)


#cProfile.run('spisok(7)')
#cProfile.run('spisok2(7)')
#cProfile.run('spisok3(7)')

#print(spisok(7))
#print(spisok2(7))
#print(spisok3(7))


# #Вывод: первое и второе решение задачи выполняется быстрее чем решение№3. Первые два работают по O(n), а третье по
# O(n**2). Из первых двух первое работает немного быстрее, но алгоритмы очень простенькие, чтобы дать точный ответ,
# что лучше в итоге использовать.
