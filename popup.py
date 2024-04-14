from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ser_obj = Service()
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
driver.find_element(By.XPATH,"//*/ol/li/span/button/svg/path").click()
time.sleep(10)
print("test pass")
