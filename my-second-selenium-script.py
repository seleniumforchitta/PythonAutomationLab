# pip install --upgrade selenium webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://parabank.parasoft.com/parabank/index.htm")
print(driver.title)  # Captures the Title
url1 = driver.title
print(driver.current_url)
driver.get("https://magento.softwaretestingboard.com/")
print(driver.title)  # Captures the Title
url2 = driver.title
print(driver.current_url)
assert url1 != url2
driver.minimize_window() #To minimize the current window - driver.manage().window().minimize()
driver.back() #diver.navigate().back() in selenium – To go back to the old page
driver.refresh()  # Refresh the loaded page
print(driver.title, driver.current_url)
driver.close()

