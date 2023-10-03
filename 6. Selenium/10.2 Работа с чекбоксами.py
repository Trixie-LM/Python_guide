import time
from selenium import webdriver


driver = webdriver.Firefox()

driver.get("https://demoqa.com/selectable")

ELEMENT_OME = ("xpath", "//li[text()='Cras justo odio']")


before = driver.find_element(*ELEMENT_OME).get_attribute("class")
print(before)
driver.find_element(*ELEMENT_OME).click()
after = driver.find_element(*ELEMENT_OME).get_attribute("class")
print(after)
assert "active" in after

time.sleep(3)
