# Чтение файла
filename = input('Укажите файл: ')
file = open(filename, 'r')

print(file.read())
print(len(file.read()) )
print('Количество символом в файле - ' + str( len(file.read())) )

file.close()

# r - Чтение файла
# w - Перезапись файла
# a - Добавление в файл

# b - binary mode - для работы с картинками, аудио и т.д

# Перезапись файла
filename = input('Укажите файл: ')
text = input('Что нужно добавить в  файл: ')
file = open(filename, 'w')

file.write(text)

file.close()


# Добавление в файл
filename = input('Укажите файл: ')
text = input('Что нужно добавить в  файл: ')
file = open(filename, 'a')

file.write(text)

file.close()



# Вывести по 8 букв на 21 строки
file = open('123.txt', 'r')

for i in range(21):
    print(file.read(8))

file.close()




# Чтение строк
file = open('123.txt', 'r')

print(file.readlines())
file.close()

# Конструкция закрывает файл в конце
with open('123.txt', 'r') as f:
    print(f.read())
