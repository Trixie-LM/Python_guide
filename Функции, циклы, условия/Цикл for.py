# 1. Подсчет конкретных букв в строке
test = 'qwertyrhthtr'
count = 0

for i in test:
    if i == 'r':
        print(i)
        count += 1

else:
    print(f'Цикл завершен! Всего букв \'r\' - {count} штуки.')

# 2. Цикл в 2-ом шаге в обратном порядке
for i in range(0, 10, 2)[::-1]:
    print(i)
