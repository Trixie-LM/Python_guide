class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def return_one(cls):
        return 1

    @staticmethod
    def make_upper(name):
        return name.upper()

    def __get_name(self):
        return self.make_upper(self.name)

    def bark(self):
        print(self.__get_name())
        print('BARK')


class ChihuaHua(Dog):
    def shit_himself(self):
        print('SHIT')


print(Dog.return_one())




basya = Dog('Basya', 5)
syama = Dog('SYAMA', 8)
shit_dog = ChihuaHua('Shitty', 1)


basya.bark()
syama.bark()
print()
shit_dog.shit_himself()
shit_dog.bark()

print(Dog.make_upper('ляляля'))


