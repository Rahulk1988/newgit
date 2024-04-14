import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):


    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("C:/driver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)


    elif browser_name == "edge":
        service_obj = Service("C:/driver/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)

    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
