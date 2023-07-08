import random


# 1. Умножение числа на 2
def multiply(number):
    print(number * 2)


# 2. Выводим большее значение
def max(x, y):
    if x > y:
        return x
    else:
        return y


print(max(4, 30))


# 3. Выводим введенное имя через дополнительную функцию
def awe():
    print("Watch in AWE " + qwe())


def qwe():
    return ('Trixie')
    # return input('Введите свое имя: ')


awe()

# 4. Проверяем тип данных
i = random.choice([64, 84.32, 'a'])
if type(i) == type(1):
    print(f'Это целое число: {i}')
elif type(i) == type(1.1):
    print(f'Это не целое число: {i}')
else:
    print(f'Выходит из условий: {i}')


# 5. Проверяем, что число больше 0 и выводим ошибку, если это не так
def test(number):
    assert number > 0, 'Номер должен быть больше 0'
    print(str(number))


test(10)


# Значение параметра по умолчанию
def my_function(country="Англии"):
    print("Я из " + country)


my_function()
my_function("Польши")
my_function("Китая")

a = 2
b = "PythonRU"
print("{0} — целое число, а {1} — строка.".format(a, ))

a = 2
b = "PythonRU"
print("%d — целое число, а %s — строка." % (a, b))
