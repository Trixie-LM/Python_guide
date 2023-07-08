names = ['Вася', 'Петя', 'Пидар']

numbers = [1, 2, 3, 4, 5]

print([name.upper() if name == 'Пидар' else name for name in names])
print([num + 1 if num == 3 else num for num in numbers])

# "list comprehension". It means something like "for each x in text, if x.isdigit() is True, add it to the list" –

text = "word1anotherword23nextone456lastone333"
numbers = [x for x in text if x.isdigit()]
print(numbers)

my_numbers = [1, 2, 3, 4, 5]
odd_numbers = [item for item in my_numbers if item % 2 == 1]
print(odd_numbers)

# values = [self.sheet.cell(row=row, column=column).value for row in range(min_row, max_row)]
# total = sum(float(v) if data_type == 'float' else int(v) for v in values)
