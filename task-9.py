from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
#go for URL
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title

#Select username
user_name=driver.find_element(By.NAME,"user-name").send_keys("standard_user")
time.sleep(3)

#select password
pass_word=driver.find_element(By.ID,"password").send_keys("secret_sauce")

#click login button
login=driver.find_element(By.ID,"login-button").click()

#check page url
assert "inventory.html" in driver.current_url

#save "Webpage_task_11.txt" file
page_source = driver.page_source
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_source)
time.sleep(5)
driver.quit()