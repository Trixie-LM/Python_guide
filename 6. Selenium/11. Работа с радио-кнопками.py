import time
from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://demoqa.com/radio-button")

ACTION_YES_RADIO = ("xpath", "//label[@for='yesRadio']")
ACTION_NO_RADIO = ("xpath", "//label[@for='noRadio']")
STATUS_YES_RADIO = ("xpath", "//input[@id='yesRadio']")
STATUS_NO_RADIO = ("xpath", "//input[@id='noRadio']")

print(driver.find_element(*ACTION_YES_RADIO).is_selected())
driver.find_element(*ACTION_YES_RADIO).click()
print(driver.find_element(*ACTION_YES_RADIO).is_selected())
time.sleep(3)

print(driver.find_element(*STATUS_YES_RADIO).is_enabled())  # True
print(driver.find_element(*STATUS_NO_RADIO).is_enabled())  # False
