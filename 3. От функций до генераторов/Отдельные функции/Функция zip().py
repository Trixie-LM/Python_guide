# Функция zip() в Python создает итератор, который объединяет элементы из нескольких источников данных.
# Эта функция работает со списками, кортежами, множествами и словарями для создания списков или кортежей, включающих все эти данные.

# У функции zip() множество сценариев применения. Например, она пригодится,
# если нужно создать набор словарей из двух массивов, каждый из которых содержит имя и номер сотрудника.


employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
zipped_list = list(zipped_values)

print(zipped_list)
print(type(zipped_values))

"""
    Использование одного аргумента 
"""
employee_names = ["Дима", "Марина", "Андрей", "Никита"]
zipped_object = zip(employee_names, '1 4')
print(list(zipped_object))

"""
    Функция zip с циклом for
"""
employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

for name, number in zip(employee_names, employee_numbers):
    print(name, number)

"""
    Как сделать «unzip»
"""

employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)

print(employee_names)
print(employee_numbers)
