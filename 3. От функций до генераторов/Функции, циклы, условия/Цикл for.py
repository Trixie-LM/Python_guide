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


# Так же вы можете записать сразу несколько операторов else на одной строке:
a = 200
b = 33
print("A") if a > b else print("=") if a == b else print("B")