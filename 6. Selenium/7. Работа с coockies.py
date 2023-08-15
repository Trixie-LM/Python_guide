import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,700")
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager(version="114.0.5735.90").install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru/login")


# Вывод 1 и всех Куки
print(driver.get_cookie("country_code"))
print(driver.get_cookies())


# Добавление Куки
driver.add_cookie({
    "name": "Test",
    "value": "Testing"
})
print(driver.get_cookie("Test"))


# Замена Куки
driver.delete_cookie("Test")
driver.add_cookie({
    "name": "Test",
    "value": "Change_testing"
})
print(driver.get_cookie("Test"))


# Сохранение Куки
# Что сохраняем, куда и операции((Write Bytes)запись в байтовом формате)
pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb"))


# Использование Куки
driver.delete_all_cookies()

# Откуда грузим и операции((Read Bytes)чтение в байтовом формате)
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "кb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
