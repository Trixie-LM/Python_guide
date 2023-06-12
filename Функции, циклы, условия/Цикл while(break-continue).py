# 1. Расчет факториала, бесконечный цикл
while True:
    number = input('Введите число для факториала: ')
    i = 0
    factorial = 1

    if number == 'stop':
        break

    while i < int(number):
        i += 1
        factorial *= i
        print(f'Шаг: {i}. Число - {factorial}')



# 2. Ввод данных побуквенно и вывод слова целиком
x = ''
while len(x) < 5:
    y = input('Введите данные: ')
    if y == 'o':
        print(f'Буква \'{y}\' не учитывается в цикле')
        continue
    if y == 'r':
        print(f'Ошибка! Некорректные данные: {y}')
        break
    x += y

else:
    print(x)
