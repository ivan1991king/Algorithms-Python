__author__ = 'Куркин Иван'

# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.

import random
print(f'Отгадайте число от 0 до 100')

num = random.randint(0, 100)
n = 10
while n > 0:
    print(f'У вас осталось {n} попыток')
    user_num = int(input('Введите число: '))
    if user_num > num:
        print("Ваше число больше")
    elif user_num < num:
        print("Ваше число меньше")
    else:
        print("Вы угадали!")
        break
    n -= 1
else:
    print(f'Вы не угадали! Это число {num}')
