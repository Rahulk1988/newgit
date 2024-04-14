from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
print(driver.title)
# 
# driver = webdriver.Edge()
# driver.maximize_window()
# driver.get("https://www.facebook.com/")
# print(driver.title)
#
# driver = webdriver.Firefox()
# driver.maximize_window()
# driver.get("https://www.facebook.com/")
# print(driver.title)

# driver = webdriver.Safari()
# driver.maximize_window()
# driver.get("https://www.facebook.com/")
# print(driver.title)