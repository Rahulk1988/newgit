import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from end_to_end.baseclass import Baseclass


# @pytest.mark.usefixtures("setup") moved in separate file to call the as parent class
class Testone(Baseclass):
    def test_e2e(self):

        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("Ber")
        time.sleep(2)
        results = self.driver.find_elements(By.XPATH, "//div[@class = 'products']/div")
        count = len(results)
        print(count)
        assert count > 0
        for result in results:
            result.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
        self.driver.find_element(By.XPATH, "//button[text()= 'PROCEED TO CHECKOUT']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div > input").send_keys(
            "rahulshettyacademy")
        self.driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
        print(self.driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div > span").text)

        prices = self.driver.find_elements(By.XPATH, "//td[5]/p")
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
        print(sum)
        totalamount = int(self.driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)
        assert sum == totalamount
        disamt = float(self.driver.find_element(By.CSS_SELECTOR, "span[class='discountAmt']").text)
        print(disamt)
        assert totalamount > disamt
        self.driver.execute_script("window.scrollTo(0, 100)")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Place Order']").click()
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "div[class='wrapperTwo'] div select"))
        dropdown.select_by_visible_text("India")
        check = self.driver.find_element(By.CSS_SELECTOR, "input[class='chkAgree']")
        check.click()
        assert check.is_selected()
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Proceed']").click()
