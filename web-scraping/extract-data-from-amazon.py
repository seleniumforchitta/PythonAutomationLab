from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.in/s?k=macbook&crid=Z9GAE8M6PAJC&sprefix=macbook%2Caps%2C240&ref=nb_sb_noss_2")
driver.maximize_window()

elem_list = driver.find_elements(By.XPATH, "//div[@data-cy='title-recipe']/a/h2/span")
print(len(elem_list))
# for i in elem_list:
#     print(i.text)