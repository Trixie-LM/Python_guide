"""
Неявное ожидание - кол-во времени в течение которого веб-драйвер будет стучаться в DOM, чтобы узнать ЕСТЬ ЛИ такой элемент

"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

# Неявное ожидание
driver.implicitly_wait(10)

driver.find_element(*VISIBLE_AFTER_BUTTON).click()


# Явное ожидание
wait = WebDriverWait(driver, 15, poll_frequency=1)
button = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON))
button.click()
