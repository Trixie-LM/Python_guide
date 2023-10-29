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


def run_task(task):
    print('Before running the task')
    task()
    print('After running the task')


run_task(lambda: print('Task is complete!'))  # передача анонимной функции
important_task = lambda: print('Important task is complete!')
run_task(important_task)  # передача лямбда-функции


# Сортировка с Лямбдой по возрасту
users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

users.sort(key=lambda user: user['age'])

print(users)