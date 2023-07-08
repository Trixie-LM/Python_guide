# 0. https://pythonru.com/osnovy/modul-json-v-python

"""
Когда вы конвертируете из Python в JSON, объекты Python преобразуются в эквивалент JSON:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
"""

# 1. Если у вас есть строка JSON, вы можете провести над ней парсинг с помощью метода json.loads ().
# Как результат, будет словарь python.
# Конвертируем из JSON в Python:


import json

# немного JSON:
x = '{"name":"Viktor", "age":30, "city":"Minsk"}'
# парсинг x:
y = json.loads(x)
# результатом будет словарь Python:
print("\nЧасть 1.")
print(y["age"])

# 2. Если у вас есть объект Python, вы можете преобразовать его в строку JSON с помощью метода json.dumps().

# создаем словарь x:
x = {
    "name": "Viktor",
    "age": 30,
    "city": "Minsk"
}
# конвертируем в JSON:
y = json.dumps(x)  # Строка
w = json.dumps(x, indent=4)  # Красивый формат
e = json.dumps(x, indent=4, separators=(". ", " = "))  # Красивый формат с измененными разделителями
# в результате получаем строк JSON:
print("\nЧасть 2.")
print(y)
print(w)
print(e)

# Используем параметр sort_keys чтобы указать, должен ли сортироваться результат.
w = json.dumps(x, indent=4, sort_keys=True)  # Красивый формат
print(w)

# 3. Как конвертировать кириллицу
# Если в данных Python есть символы кириллицы, метод json.dumps() преобразует их с кодировкой по умолчанию.
# Чтобы сохранить кириллицу используйте параметр ensure_ascii=False
import json

x = {
    "name": "Виктор"
}
y = {
    "name": "Виктор"
}
print("\nЧасть 3.")
print(json.dumps(x))
print(json.dumps(y, ensure_ascii=False))
