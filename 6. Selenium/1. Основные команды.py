"""
    from webdriver_manager.chrome import ChromeDriverManager - позволяет автоматически скачивать актуальную версию драйвера
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.firefox import GeckoDriverManager - драйвер браузера FIREFOX
"""
import time
from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Настройки для Хрома
service = Service(executable_path=ChromeDriverManager().install())

# Настройки для Хрома с определенной версией драйвера
service2 = Service(ChromeDriverManager(version="114.0.5735.90").install())

driver = webdriver.Chrome(service=service)

# Настройки для Firefox с определенной версией драйвера
driver2 = webdriver.Firefox()

# Выбор хром драйвера из определенного места. Нужен если хромдрайвера нет в общем доступе, как в моем случае
service = Service('chromedriver.exe')
driver3 = webdriver.Chrome(service=service)



# Открываем сайт
driver.get("https://www.youtube.com/")

time.sleep(3)


# Текущая ссылка сайта
print("Ссылка сайта: ", driver.current_url)

# Текущий тайтл страницы
print("Название страницы: ", driver.title)

# Получение кода страницы
print("Название страницы: ", driver.page_source)


# Возвращаемся назад
driver.back()

# Возобновляем шаг
driver.forward()

# Перезагрузка страницы
driver.refresh()


"""
    Поиск
    －Способы поиска эквивалентные By.***, например By.XPATH:
    * ID = "id"
    * XPATH = "xpath"
    * NAME = "name"
    * CLASS_NAME = "class name"
    * CSS_SELECTOR = "css selector"
"""

button = driver.find_element("xpath", "//input[@name='password']")
# Клик по кнопке
button.click()

# Вводим значение с клавиатуры
button.send_keys("Значение какое-то")

# Получаем введеное значение в поле button
print(button.get_attribute("value"))

# Очистка поля
button.clear()

# Нажать ENTER
button.send_keys(Keys.RETURN)

# Создает список с тегами a и кликаем на 3 элемент
button = driver.find_element("xpath", "//a")[2].click()


"""
    driver.window_handles - выводит список вкладок
    driver.switch_to.window(driver.window_handles[0]) - переключение к 1 вкладке
    driver.current_window_handle - возвращает дескриптор текущей вкладки; 
    
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") - скролл в конец страницы
"""