# Функция main() используется для разделения блоков кода в программе.
# Использование функции main() обязательно в таких языках, как Java, потому что это упрощает понимание того, в каком порядке код запускается в программе.
# Python функцию main() писать необязательно, но это улучшает читаемость кода.


def choose_username():
    global username
    username = input("Введите логин: ")
    if len(username) > 5:
        print("Ваш логин сохранен.")
    else:
        print("Пожалуйста, выберите имя пользователя длиной более пяти символов.")
        choose_username()


def print_username():
    print(username)


def main():
    choose_username()
    print_username()


if __name__ == "__main__":
    main()
