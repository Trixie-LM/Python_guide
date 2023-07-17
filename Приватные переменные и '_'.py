# Приватные переменные — это те переменные, к которым можно получить доступ внутри класса, где они были объявлены.
# В Python для этого есть одиночные и двойные подчеркивания, хотя вторые используются куда чаще.
# С их помощью можно получать доступ изнутри класса и выполнять «искажение имен».


class Mainclass:
    __private_variable = 2020

    def __private_method(self):
        print("Это приватный метод")

    def insideclass(self):
        print("Приватная переменная:", Mainclass.__private_variable)
        self.__private_method()

foo = Mainclass()
foo.insideclass()



class Vehicle:
    def _start_engine(self):
        return "Создаем мотоцикл."

    def run(self):
        return self._start_engine()
if __name__ == '__main__':
    bike = Vehicle()
    print(bike._start_engine())
    print("Мотоцикл создан.")
    bike.run()
    print("Мотоцикл запущен.")