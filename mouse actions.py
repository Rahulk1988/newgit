import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(2)
action = ActionChains(driver)

action.double_click(driver.find_element(By.ID, "checkBoxOption1")).perform()

driver.execute_script("window.scrollBy(0,200)")
time.sleep(2)
action.move_to_element(driver.find_element(By.XPATH,"//button[@id ='mousehover']")).perform() # ---mouse hover
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform() # ---need to do both
# action.context_click(pass the element location).perform() #---rightclick
