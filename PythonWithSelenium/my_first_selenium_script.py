# pip install --upgrade selenium webdriver-manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window();

driver.get('https://ultimateqa.com/automation')
time.sleep(5)  # Let the user actually see something!

driver.find_element(By.XPATH, "//a[contains(text(), 'Learn how to automate an application that evolves over time')]").click()

appLandingText = driver.find_element(By.XPATH, "//h1[@class='entry-title main_title']").text
assert appLandingText == "Sample Application Lifecycle – Sprint 1"

search_box = driver.find_element(By.NAME, 'firstname')  # Corrected By.NAME usage
search_box.send_keys('Automation')
search_box.submit()

time.sleep(5)  # Let the user actually see something!
searchLandingText = driver.find_element(By.XPATH, "//h1[@class='et_pb_module_heading']").text
assert searchLandingText == "Push Higher Quality Software To Market Faster"

print(driver.title)

# driver.quit()
