import time
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

driver.get("https://demoqa.com/alerts")

# # Принятие алерта
# BUTTON_1 = ("xpath", "//button[@id='alertButton']")
# wait.until(EC.element_to_be_clickable(BUTTON_1)).click()
#
# alert = wait.until(EC.alert_is_present())
#
# driver.switch_to.alert
#
# alert.accept()
# time.sleep(3)


# # Отклонение и получение текста алерта
# BUTTON_3 = ("xpath", "//button[@id='confirmButton']")
# wait.until(EC.element_to_be_clickable(BUTTON_3)).click()
#
# alert = wait.until(EC.alert_is_present())
#
# driver.switch_to.alert
# print(alert.text)
# alert.dismiss()
# time.sleep(3)


# Ввод текста в поле алерта
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.send_keys("Testing")
alert.accept()

time.sleep(3)
