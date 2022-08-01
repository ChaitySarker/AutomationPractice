import time
from selenium.webdriver.common.by import By


class SignIn:
    def __init__(self, driver):
        self.driver = driver

    def signin_page(self):

        # Click Sign in Button
        signin_btn = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        signin_btn.click()
        time.sleep(2)