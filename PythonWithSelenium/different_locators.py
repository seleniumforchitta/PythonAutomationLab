import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window();

driver.maximize_window()
driver.get("https://sso.teachable.com/secure/9521/identity/login/password")

email = "demo@gmail.com"

driver.find_element(By.XPATH, "//input[@id='email']").send_keys(email)
driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(2)
output = driver.find_element(By.XPATH, "//div[@id='otp-login']/div/div/p").text
assert email in output
if email in output:
    print("Test is Passed !")
driver.close()
