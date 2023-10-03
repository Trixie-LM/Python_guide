import random


print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))

# При помощи seed генерятся данные, которые никогда не изменятся, пока не изменено слово
random.seed('Ponies')
print('Статичные данные от теста к тесту')
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
print(random.randint(0, 100))
