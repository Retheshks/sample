from unittest import TestCase
from selenium.webdriver import Chrome

class TestLoginLogin(TestCase):

    def test_login_with_valid_credentials(self):
        driver = Chrome("F:/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://demo.actitime.com")

        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_name('pwd').send_keys('manager')
        driver.find_element_by_id('loginButton').click()
