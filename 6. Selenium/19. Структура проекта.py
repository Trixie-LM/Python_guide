"""
    Директории:
    1. Base - основная структура кода.
    2. Utilities - повторяющиеся функции для Base
    3. TestCases - тест-кейсы
    4. ConfigFile - настройки, например браузер
    5. TestData - данные для запуска селениума
    6. Logs - логи
    7. Reports - отчеты


    1. В ней находятся webDriver элементы. Нужен для того, чтобы функционал кода был переиспользован в других TestCases

    3.1. Модуль conftest - тут находятся фикстуры, которые выполняются до начала основного кода
    3.2. Чтобы перекинуть проперти, такие как driver из conftest в основной файл test_multibonus, мы задаем фикстуру request в функции authorization
    3.3 Находясь в test_multibonus, нужно зайти в Edit Configuration и выбрать модуль test_multibonus. Только так запустится код

    @pytest.fixture(scope="class")
    def authorization(request):
"""