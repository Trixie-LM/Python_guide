"""
Блок try позволяет проверить блок кода на ошибки.
Блок except обрабатывает ошибку.
Блок finally позволяет выполнять код, независимо от результата блоков try и except.
"""

import random

random_number = random.randint(1, 5)
user_number = input("Угадай число (от 1 до 5): ")

if int(user_number) == random_number:
    print("Красавчик! Угадал!")
else:
    print(f"Не повезло. \nВы ввели: {user_number}. А число было: {random_number}")

try:
    eval('print( 5 / 0)')
except ZeroDivisionError:
    print("Дурак? Зачем на 0 делишь?")
except:
    print("Какая-то ошибка....")
finally:
    print("Вот и все")

try:
    print(5 / 0)
except:
    pass
