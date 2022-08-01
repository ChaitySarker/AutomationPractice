import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from Framework.page.create_new_account import CreateAccountPage
from Framework.page.sign_in import SignIn
from Framework.page.signup_page import SignUp


class CreateAccountTest(unittest.TestCase):
    def test_create_account(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(2)

        signin = SignIn(driver)
        signin.signin_page()

        signup = SignUp(driver)
        signup.signup_page("chaity228@gmail.com")

        cap = CreateAccountPage(driver)
        cap.create_account("Mrs.", "Chaity","sk" "@@%%BDtest%%@@", "bjit", "Baridhara,Ghulshan,Dhaka","khulna", "00000",
                          "AdditionalInform", "26364656", "01920692424", "dhaka")

        # Screenshot
        driver.save_screenshot("F:\\SQA\\Class\\Project\\TestAutomationProject\\Framework\\Screenshot\\Create_New_Account.png")

        driver.close()
