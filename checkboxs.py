# import time
import time

# import alter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
# checkbox = driver.find_element(By.CSS_SELECTOR, "input[ID='ctl00_mainContent_rbtnl_Trip_1']")
# checkbox.click()
# time.sleep(2)
# assert checkbox.is_enabled()

# Additional pop-up with html code
checkbox = driver.find_element(By.CSS_SELECTOR, "input[ID='ctl00_mainContent_rbtnl_Trip_2']")
checkbox.click()
time.sleep(2)
assert checkbox.is_enabled()

driver.find_element(By.ID, "MultiCityModelAlert").click()

# text = driver.find_element(By.ID, "autosuggest").is_displayed()
# print(text)
assert driver.find_element(By.ID, "autosuggest").is_displayed()


# radios=driver.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
# for radio in radios:
#         if radio.find_element(By.NAME, "ctl00$mainContent$chk_friendsandfamily") == "Senior Citizen":
#             radio.click()
#              # assert radio.get_attribute("value") == "One way"
#             break

