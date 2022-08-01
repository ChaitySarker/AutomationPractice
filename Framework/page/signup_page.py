import time
from selenium.webdriver.common.by import By


class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def signup_page(self, email):

        # Input Email Address
        email_address = self.driver.find_element(By.ID, 'email_create')
        email_address.send_keys(email)

        # Click Create an Account Button
        create_acc_button = self.driver.find_element(By.ID, 'SubmitCreate')
        create_acc_button.click()
        time.sleep(2)