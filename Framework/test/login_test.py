import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from Framework.page.sign_in import SignIn
from Framework.page.login import LoginPage


class Login_test(unittest.TestCase):

    def test_login(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseURL)
        time.sleep(2)

        signin = SignIn(driver)
        signin.signin_page()

        lp = LoginPage(driver)
        lp.login_page("chaitycatseye@gmail.com", "@@%%BDtest%%@@")
        time.sleep(5)

        # Screenshot
        driver.save_screenshot("F:\\SQA\\Class\\Project\\TestAutomationProject\\Framework\\Screenshot\\Login_test.png")

        driver.close()
