"""
Метод	        Значение
clear()	        Удаляет все элементы из словаря
copy()	        Делает копию словаря
fromkeys()	    Возвращает словарь с указанными ключами и значениями
get()	        Возвращает значение по ключу
items()	        Возвращает список, содержащий tuple для каждой пары ключ-значение
keys()	        Возвращает список, содержащий ключи словаря
pop()	        Удаляет элементы по ключу
popitem()	    Удаляет последнюю пару ключа со значением
setdefault()	Задает значение по ключу. Если ключа нет в словаре, добавляет его с указанным значением или None
update()	    Обновляет словарь, добавляя пары ключ-значение
values()	    Возвращает список всех значений в словаре

"""
# Создание словаря
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# обратите внимание, ключевые слова не являются строками
# обратите внимание на использование "рвно", вместо двоеточия для задания
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Доступ к элементам
x = thisdict["model"]
y = thisdict.get("model")
print(x, "<-x - y->", y)

# Изменить значение
thisdict["year"] = 2018
print(thisdict)

# Цикл for по словарю выводит ключи
for x in thisdict:
    print("Ключ: ",x)

# Цикл for по словарю выводит значения
for x in thisdict:
    print("Значение: ", thisdict[x])

for x in thisdict.values():
    print("Значение .values(): ", x)

for x, y in thisdict.items():
    print(x, ":", y)

# Добавление элементов
thisdict["color"] = "red"
print(thisdict)



