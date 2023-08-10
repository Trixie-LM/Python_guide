"""
zip_longest() — функция модуля itertools, которая используется для объединения двух итерируемых объектов.

zip_longest() лучше обычного zip()  (https://t.me/xo_py/281)тем, что zip_longest() расширяет итерируемые объекты до одинаковой длины.
Если одно из итерируемых объектов имеет большую длину, чем другой, то функция zip_longest() использует значение fillvalue(по умолчанию None)
для заполнения отсутствующих элементов.
"""

from itertools import zip_longest


employee_names = ["Дима", "Марина", "Андрей", "Никита"]
employee_numbers = [2, 9, 18]


zipped_values = zip_longest(employee_names, employee_numbers, fillvalue='UNKNOWN')

for name, age in zipped_values:
    print(f"Name: {name}, Age: {age}")


