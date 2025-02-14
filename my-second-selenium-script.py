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
url1 = driver.title
print("URL of the landing page - ",driver.title, driver.current_url)
driver.get("https://google.com/")
url2 = driver.title
print("URL of the newly loaded page - ",driver.title, driver.current_url)
assert url1 != url2
driver.back() #diver.navigate().back() in selenium – To go back to the old page
driver.refresh()  # Refresh the loaded page
print("URL after the it is refresahed back - ",driver.title, driver.current_url)
driver.forward() 
driver.refresh() 
print("URL after the it is refresahed forward - ",driver.title, driver.current_url)
driver.minimize_window() #To minimize the current window - driver.manage().window().minimize()
driver.close()

