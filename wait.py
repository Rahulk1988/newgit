import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/driver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("Ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
count = len(results)
print(count)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text()= 'PROCEED TO CHECKOUT']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#root > div > div > div > div > div > input").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div > span").text)

prices = driver.find_elements(By.XPATH,"//td[5]/p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
totalamount = int(driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)
assert sum == totalamount
disamt = float(driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']").text)
print(disamt)
assert totalamount > disamt
driver.execute_script("window.scrollTo(0, 100)")
driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
dropdown = Select(driver.find_element(By.CSS_SELECTOR,"div[class='wrapperTwo'] div select"))
dropdown.select_by_visible_text("India")
check = driver.find_element(By.CSS_SELECTOR,"input[class='chkAgree']")
check.click()
assert check.is_selected()
driver.find_element(By.XPATH,"//button[normalize-space()='Proceed']").click()