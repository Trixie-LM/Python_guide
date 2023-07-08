# Отдельное внимание будет уделено инструкции yield. Она является частью генератора и заменяет ключевое слово return.
# Когда программа доходит до yield, то функция переходит в состояние ожидания и продолжает работу с того же места при повторном вызове.

def fibonacci(xterms):
    # первые два условия
    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
        print("Укажите целое число больше 0")
    elif xterms == 1:
        print("Последовательность Фибоначчи до", xterms, ":")
        print(x1)
    else:
        while count < xterms:
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth

fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))


# Создаем список
alist = [4, 16, 64, 256]

# Вычислим квадратный корень, используя генерацию списка
out = [a**(1/2) for a in alist]
print(out)

# Используем выражение генератора, чтобы вычислить квадратный корень
out = (a**(1/2) for a in alist)
print(out)
print(next(out))
print(next(out))
print(next(out))
print(next(out))
