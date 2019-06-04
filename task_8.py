__author__ = 'Куркин Иван'
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


def generate_matr(rows, cols):
    matr = []
    for i in range(rows):
        row = []
        summa = 0
        for j in range(cols-1):
            row.append(int(input(f"Введите элемент матрицы [{i}][{j}] : ")))
            summa = summa+row[j]
        row.append(summa)
        matr.append(row)
    return matr

matr54 = generate_matr(5,4)

for line in matr54:
    print(line)
