from selenium import webdriver
from selene.support.shared import browser
from selene import be, have, command


# Открытие браузера
browser.open('https://google.com')
# Закрытие браузера
browser.quit()

# Увеличение окна браузера на максимум
browser.driver.maximize_window()

# Выбор браузера. По умолчанию Хром.
driver_options = webdriver.FirefoxOptions()
driver_options.add_argument('--headless')
browser.config.driver_options = driver_options


# Общий тайм-аут браузера
browser.config.timeout = 3.0
# Тайм-аут
browser.all('#APjFqb').with_(timeout=4).should(have.size(5))


# Поиск по XPATH
browser.element('//li')
# Находит 1 элемент по селектору
browser.element('#APjFqb')
# Находит все элементы по селектору
browser.all('#APjegRd')


# Проверка поля на пустоту и нажатие Энтера
browser.element('#APjFqb').should(be.blank).type('yashaka/selene').press_enter()
# Проверка поля на определенный текст
browser.element('#search').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))
# Проверка у коллекции ровно 3 элемента и содержит именно тот текст, что указан
browser.all('#APjegRd').should(have.exact_texts('a', 'b', 'c'))


# Завязка на текст. Находим 1 элемент с конкретным текстом и кликаем
browser.all('#APjegRd').element_by(have.exact_text('a')).click()
# Завязка на класс. Находим все элементы с добавленным классом completed и кликаем
browser.all('#APjegRd').by(have.css_class('completed')).click()
# Завязка на класс. Отрицание. Находим все элементы у которых нет класса completed и кликаем
browser.all('#APjegRd').by(have.no.css_class('completed')).click()

# Написать в поле с id=userName слово Trixie
browser.element('#userName').type('Trixie')


# Ждем до какого то момента
browser.all('#APjFqb').wait.for_(have.size(3))

# Выделить весь текст
browser.element('#userName').perform(command.select_all)

# Все вводы текста будут через JS
browser.config.type_by_js = True

# Скролл к нужному элементу
browser.element('#userNumber').perform(command.js.scroll_into_view)

# Удаление части элемента на странице
browser.element('//footer').perform(command.js.remove)


