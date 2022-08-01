import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from Framework.page.login import LoginPage
from Framework.page.sign_in import SignIn
from Framework.page.t_shirt_page import TShirtPage
from Framework.page.payment_process_page import PaymentProcessPage


class Tshirt_SelectionTest(unittest.TestCase):

    def test_tshirt_selection(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        signin = SignIn(driver)
        signin.signin_page()

        lp = LoginPage(driver)
        lp.login_page("chaitycatseye@gmail.com", "@@%%BDtest%%@@")
        time.sleep(3)

        tsp = TShirtPage(driver)
        tsp.t_shirt_page()
        time.sleep(5)

        # Screenshot
        driver.save_screenshot("F:\\SQA\\Class\\Project\\TestAutomationProject\\Framework\\Screenshot\\T-shirt_selection.png")

        ppp = PaymentProcessPage(driver)
        ppp.payment_process()
        time.sleep(3)

        # Screenshot
        driver.save_screenshot("F:\\SQA\\Class\\Project\\TestAutomationProject\\Framework\\Screenshot\\Sign_out.png")
