import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from Framework.page.login import LoginPage
from Framework.page.sign_in import SignIn
from Framework.page.casual_dress_selection_page import DressSelectionPage


class Dress_SelectionTest(unittest.TestCase):
    def test_dress_selection(self):
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

        dsp = DressSelectionPage(driver)
        dsp.dress_selection()
        time.sleep(5)

        # Screenshot
        driver.save_screenshot("F:\\SQA\\Class\\Project\\TestAutomationProject\\Framework\\Screenshot\\Casual_dress_selection.png")
