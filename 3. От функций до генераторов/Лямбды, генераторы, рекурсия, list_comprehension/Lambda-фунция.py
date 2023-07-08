# https://habr.com/ru/companies/piter/articles/674234/

# Лямбда-функция — это небольшая анонимная функция. Она может принимать любое количество аргументов,
# но в то же время иметь только одно выражение.

x = lambda a, b: a * b
print(x(8, 9))

# Силу лямбда лучше видно, когда вы используете ее как анонимную функцию внутри другой функции

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

# Лямбда и условные операторы
max_number = lambda a, b: a if a > b else b
print(max_number(3, 5))


