"""
https://www.youtube.com/watch?v=lfsyd08aXOg&ab_channel=AlekseiKoledachkin
"""

import time
from selenium import webdriver


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/checkboxes")

CHECKBOX_1 = ("xpath", "//input[1]")

first_checkbox = driver.find_element(*CHECKBOX_1)
print(first_checkbox.get_attribute("checked"))  # None
print(first_checkbox.is_selected())  # False
time.sleep(3)

# Проставление чекбокса
first_checkbox.click()
time.sleep(3)

# Получение статуса чекбокса
print(first_checkbox.get_attribute("checked"))  # true
print(first_checkbox.is_selected())  # True
