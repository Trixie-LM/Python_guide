# Функция filter() в Python применяет другую функцию к заданному итерируемому объекту (список, строка, словарь и так далее),
# проверяя, нужно ли сохранить конкретный элемент или нет.
# Простыми словами, она отфильтровывает то, что не проходит и возвращает все остальное.

# Функция filter() принимает два параметра. Первый — имя созданной пользователем функции,
# а второй — итерируемый объект (список, строка, множество, кортеж и так далее).

# filter(in_function|None, iterable)
# |__filter object

"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))


"""
    Программа для поиска совпадений между
    двумя списками, используя функцию filter()
"""

# Список строк с похожими элементами
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True

# Применение filter() для удаления повторяющихся строк
ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))

print("Отфильтрованный список:", out_filter)



"""
    Программа для удаления стоп-слов
    из строки используя функцию filter()
"""

# Список стоп-слов
list_of_stop_words = ["в", "и", "по", "за"]

# Строка со стоп-словами
string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."

# lambda-функция, фильтрующая стоп-слова
split_str = string_to_process.split()
filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))

print("Отфильтрованная строка: ", filtered_str)



"""
    Программа для поиска общих элементов в двух списках
    с использованием функции lambda и filter()
"""

# Два массива, имеющие общие элементы
arr1 = ['p', 'y', 't', 'h', 'o', 'n', ' ', '3', '.', '0']
arr2 = ['p', 'y', 'd', 'e', 'v', ' ', '2', '.', '0']

# Лямбда с использованием filter() для поиска общих значений
def interSection(arr1, arr2): # find identical elements
   out = list(filter(lambda it: it in arr1, arr2))
   return out
# функция main
if __name__ == "__main__":
   out = interSection(arr1, arr2)
   print("Отфильтрованный список:", out)




"""
    Вызов функции filter() без функции
"""

# Список значений, которые могут быть True или False
bools = ['bool', 0, None, True, False, 1, 1-1, 2%2]

# Передали None вместо функции в filter()
out = filter(None, bools)

# Вывод результата
for iter in out:
    print(iter)
