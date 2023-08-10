from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()

# Безголовый режим для быстрых тестов и работы браузера в фоне
# options.add_argument("--headless")

options.add_argument("--incognito")  # Режим Инкогнито. Не использует кэш и не сохраняет данные
options.add_argument("--ignore-certificate-errors")  # Игнорирование SSL-сертификата
options.add_argument("--window-size=700,700")  # Размер окна
options.add_argument("--disable-cache")  # Отключение кеша

# Стратегия загрузки страницы
options.page_load_strategy = "eager"  # Отрабатывает быстрее, при загрузке структуры DOM
options.page_load_strategy = "normal"

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


# Изменений размера окна
driver.set_window_size(1920, 1080)
driver.maximize_window()  # Максимальный размер окна

# Открываем сайт
driver.get("https://whatismyipaddress.com/")
