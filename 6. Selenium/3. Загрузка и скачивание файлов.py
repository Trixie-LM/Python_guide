import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()

# СКАЧИВАНИЕ
prefs = {
    "download.default_directory": f"{os.getcwd()}/downloads"  # Устанавливаем путь для скачивания файлов
}
options.add_experimental_option("prefs", prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")

time.sleep(3)

driver.find_elements("xpath", "//a")[3].click()

time.sleep(3)


# ЗАГРУЗКА

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(3)

upload_field = driver.find_elements("xpath", "//input[@type='file']")[3]
upload_field.send_keys(f"{os.getcwd()}/downloads/2.jpg")

time.sleep(3)