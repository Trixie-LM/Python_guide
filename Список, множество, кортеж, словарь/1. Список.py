"""
Метод	    Значение
append()	Добавляет элемент(ы) в конец списка
clear()	    Удаляет все элементы в списке
copy()	    Возвращает копию списка
count()	    Возвращает число элементов с определенным значением
extend()	Добавляет элементы в конец текущего списка
index()	    Возвращает индекс первого элемента с определенным значением
insert()	Добавляет элемент по индексу
pop()	    Удаляет элемент по индексу или последний
remove()	Удаляет элементы по значению
reverse()	Разворачивает список
sort()	    Сортирует список
"""


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list(начало:конец:шаг)
var1 = digits[4]
var2 = digits[2:5]
var3 = digits[:3]
var4 = digits[5:]
var5 = digits[::2]
var6 = range(2, 20)[::2]
var7 = digits[-4]
var8 = digits[::-1]

print(var1)
print(var2)
print(var3)
print(var4)
print(var5)
for i in var6:
    print("var6: "+str(i))
print(var7)
print(var8)

# 1. Общее обращение
numbers = [1, 5, 7, 2, 1, 5, 9, 'test', 'abs', [1, 2, 3], ['q', 'w', 'e']]

print(numbers[4])
print(numbers[9])
print(numbers[9][1])
print(len(numbers))

t = list('string')
print(t)

# 2. Создание списка из списка
n = list(range(5))
m = []
print(n)
for i in n:
    if i == 3:
        continue
    print(i)
    m += [i]

else:
    print(m)

# 3. Доп методы со списком
numbers = [1, 5, 7, 2, 1]
# Добавление числа в конец списка
numbers.append(73)
print("\nДобавление числа 73 в конец списка: " + str(numbers))
# Добавление числа в конкретный индекс
numbers.insert(1, 81)
print("Добавление числа 81 в индекс 1: " + str(numbers))
# Добавление числа в конкретный индекс
print("Длина списка: " + str(len(numbers)))
# Сколько дубликатов числа 1
print("Подсчет дубликатов числа 1: " + str(numbers.count(1)))
# Сортировка
numbers.sort()
print("Сортировка: " + str(numbers))

numbers.reverse()
print("Поворот списка задом-наперед: " + str(numbers))
# Удаление
numbers.pop()
print("Удаление последнего элемента: " + str(numbers))

numbers.remove(73)
print("Удаление числа 73: " + str(numbers))

numbers.clear()
print("Очищение всего списка: " + str(numbers))

powers = ['Магия', 'Доброта', 'Верность', 'Честность', 'Смех', 'Щедрость']
ponies = 'Сумрачная искорка,Розовый пирог,Водка,Редкость,Радуга,Скромняшка'

print("\nОбъединение списка в строку:\n" + ','.join(powers))
print('-'.join(powers)+"\n")

print("Разделение строки в список:\n", ponies.split(','))

