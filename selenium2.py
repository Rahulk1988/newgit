import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# here we can create the Xpath with tag-name only
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("demo123")
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("demo123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# driver.find_element(By.XPATH, "//button[@text='Save New Password']").click()   use can use this too
time.sleep(5)
