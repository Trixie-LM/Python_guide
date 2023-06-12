import io

"""
Программа берет 2 файла под названиями "1.txt" и "2.txt" и соединяет их построчно через разделитель ", ",
соединяя полученный результат в новый файл "3.txt"
"""
with \
        io.open('1.txt', 'r', encoding='utf-8') as f1, \
        io.open("2.txt", 'r', encoding='utf-8') as f2, \
        io.open("3.txt", "w", encoding='utf-8') as f3:
    for p in zip(f1, f2):
        print(*map(lambda s: s.strip(), p), sep=', ', file=f3)
