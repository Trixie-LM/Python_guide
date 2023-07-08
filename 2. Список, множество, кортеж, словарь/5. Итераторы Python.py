# List, tuple, dict и sets — это все итерируемые объекты. Они являются итерируемыми контейнерами,
# из которых вы можете получить итератор. Все эти объекты имеют метод iter(), который используется для получения итератора.
# Получим итератор из кортежа и выведем каждое значение

mytuple = ("яблоко", "банан", "вишня")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Чтобы создать объект/класс в качестве итератора, вам необходимо реализовать методы __iter__() и __next__() для объекта.

# Как вы узнали из урока «Классы и объекты Python», у всех классов есть функция под названием __init__(),
# которая позволяет вам делать инициализацию при создании объекта.
# Метод __iter__() действует аналогично, вы можете выполнять операции (инициализацию и т. Д.),
# Но всегда должны возвращать сам объект итератора. Метод __next __ () также позволяет вам выполнять операции и должен возвращать следующий элемент в последовательности.
# Создайте итератор, который возвращает числа, начиная с 1, и увеличивает на единицу (возвращая 1,2,3,4,5 и т. д.):

class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 5
        return x


myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Приведенный выше пример будет продолжаться вечно, пока вы вызываете оператор next() или если используете в цикле for.
# Чтобы итерация не продолжалась вечно, мы можем использовать оператор StopIteration.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)
