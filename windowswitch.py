from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get()