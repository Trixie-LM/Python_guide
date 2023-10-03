"""
Метод	                        Значение
add(x)	                        Добавляет элементы x в set
clear()	                        Удаляет элементы из set
copy()	                        Возвращает копию set
x.difference(y)	                Возвращает множество элементов, которые есть в х, но нет в y
x.difference_update(y)	        Удаляет элементы, которые есть в x и y
x.intersection(y)	            Возвращает множество, являющийся пересечением x и y
intersection_update(y)	        Удаляет элементы в множестве, которых нет в других заданных y
x.isdisjoint(y)	                True, если x и y не имеют общих элементов
x.issubset(y)	                True, если все элементы из x есть в y
issuperset()	                True, если все элементы из y есть в x
pop()	                        Удаляет и возвращает последний элемент
x.symmetric_difference(y)	    Возвращает множество элементов, которые не пересекаются в х и y
symmetric_difference_update()	Добавляет элементы, которых нет в другом множестве
union()	                        Объединяет несколько множеств
x.update(y, z)	                Объединяет несколько множеств, перезаписывая x

remove()	                    Удаляет указанный элемент
    Если элемент, который нужно удалить не существует, remove() вызовет ошибку.

discard(x)	                    Удаляет указанный элемент
    Если элемент для удаления не существует, discard() не будет вызывать ошибку.
"""
# Множество не упорядочены, поэтому элементы будут отображаться в произвольном порядке при каждой обработке.
# Нельзя изменять элементы множества, но можно добавлять новые.
# Содержит только уникальные значение

# Есть так же возможность использовать конструктор set() для создания множества.
thisset = set(("ee", "list", "tuple"))  # Используем двойные скобки
print(thisset)

# Множество хранит только уникальные элементы
thisset = {"set", "list", "tuple", "list"}
print(thisset)

# Вы не можете получить доступ к элементам множества по индексу, так как они не упорядочены, а элементы без индекса.
# Но вы можете проходить по множеству с помощью цикла for или уточнять есть ли значение в множестве,
# используя оператор in.

thisset = {"set", "list", "tuple"}
for x in thisset:
    print(x)

# Добавление элемента
thisset = {"set", "list", "tuple"}
thisset.add("dict")
print(thisset)

# Длина множества
thisset = {"set", "list", "tuple"}
print(len(thisset))

# Удаление элементов
thisset = {"set", "list", "tuple"}
thisset.remove("list")
print(thisset)
