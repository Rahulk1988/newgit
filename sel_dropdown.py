import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service = service_obj)

##Static dropdown
# driver.get("https://rahulshettya cademy.com/angularpractice/")
# driver.maximize_window()
# dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_index(1)
# time.sleep(2)
# dropdown.select_by_visible_text("Male")
# time.sleep(5)

# Dynamic dropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.XPATH, "//ul/li/a")
for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"




