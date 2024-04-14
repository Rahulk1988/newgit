from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj = Service()
import time
driver = webdriver.Chrome(service=ser_obj)

# foacebook login
# driver.get("https://www.facebook.com/login/")
# driver.maximize_window()
#
# driver.find_element(By.NAME, "email").send_keys("rkneemleaf@gmail.com")
# driver.find_element(By.NAME,"pass").send_keys("momdadbros")
# driver.find_element(By.NAME,"login").click()
# time.sleep(10)
# driver.close()

# Title is not covered in facebook


# Admin-demo ID and NAME Locators
# driver.get("https://admin-demo.nopcommerce.com/login/")
# driver.maximize_window()
# driver.find_element(By.ID, "Email").clear()
# driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
# driver.find_element(By.NAME, "Password").clear()
# driver.find_element(By.NAME,"Password").send_keys("admin")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# time.sleep(10)
# print("Test is passed")
#
# driver.close()


# Link text and partial link text
# driver.get("https://www.facebook.com/login/")
# driver.find_element(By.LINK_TEXT,"Forgotten account?").click()
# print("Test is passed")
# time.sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
# time.sleep(2)
# print("Test is passed")
#
# print(driver.title)
# print(driver.current_url)
# time.sleep(2)
# driver.close()


# driver.get("https://opensource-demo.orangehrmlive.com/")

# driver.find_element(By.NAME, "username").send_keys("Admin")
#
# # driver.find_element(By.NAME,"password").send_keys("admin123")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# driver.maximize_window()

# check box single box
driver.get("https://mixitup-webflow-tutorial.webflow.io/dynamix-checkboxes")
driver.maximize_window()
time.sleep(2)
# driver.find_element(By.ID,"filter-1").click()
# time.sleep(5)

# multiple check box
checkboxs=driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id,'filter-')]")
print(len(checkboxs))
# approach 1 using range function and index
for i in range(len(checkboxs)):
    checkboxs[i].click()
time.sleep(5)

# approach 2 using without range and index
# for i in checkboxs:
#     i.click()

# approach 3 based on choice need to try
# for i in checkboxs:
#     x = i.get_attribute("ID")
#     if x == "filter-1" and x == "filter-2":
#         i.click()


# multiple checkboxs


