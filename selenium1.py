# import time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# print(driver.title)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("rahul")
driver.find_element(By.NAME, "email").send_keys("khichadirahul@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123123")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH, "//input[@value='Submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-dismissible").text
print(message)
assert "Success" in message
time.sleep(2)
