squares = [x**2 for x in range(1, 11)]

print(squares)

for index, value in enumerate(squares):
    print(f"{index}: {value}")
