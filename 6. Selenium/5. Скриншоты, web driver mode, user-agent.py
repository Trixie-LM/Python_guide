"""
Актуальные user-agent: https://www.useragents.me/

"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,700")
# Аргумент отключения видимости, что ты бот на сайте
options.add_argument("--disable-blink-features=AutomationControlled")
# Аргумент изменения user-agent
options.add_argument("--user-agent=Twilight-Sparkle")

driver = webdriver.Firefox()
driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
wait = WebDriverWait(driver, 15, poll_frequency=1)

# Сохранение скриншота
driver.save_screenshot("screen.png")
