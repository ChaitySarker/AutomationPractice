import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class PaymentProcessPage:
    def __init__(self, driver):
        self.driver = driver

    def payment_process(self):
        checkout = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
        self.driver.implicitly_wait(3)
        checkout.click()
        time.sleep(2)

        proceed_to_checkout = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button')
        self.driver.implicitly_wait(3)
        proceed_to_checkout.click()
        time.sleep(2)

        checkbox = self.driver.find_element(By.ID, 'cgv')
        checkbox_status = checkbox.is_selected()
        if not checkbox_status:
            checkbox.click()
        time.sleep(2)

        pt_checkout = self.driver.find_element(By.XPATH, '//*[@id="form"]/p/button')
        self.driver.implicitly_wait(3)
        pt_checkout.click()

        pay_by_check = self.driver.find_element(By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
        self.driver.implicitly_wait(3)
        pay_by_check.click()

        message = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/form/div/h3')
        time.sleep(2)

        display = message.is_displayed()
        if display is True:
            print('Item has successfully checked out')
        else:
            print('Item not checked out')

        confirm = self.driver.find_element(By.XPATH, '//*[@id="cart_navigation"]/button')
        self.driver.implicitly_wait(3)
        confirm.click()

        sign_out = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        self.driver.implicitly_wait(3)
        sign_out.click()