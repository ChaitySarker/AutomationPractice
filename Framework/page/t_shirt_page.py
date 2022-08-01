import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class TShirtPage:
    def __init__(self, driver):
        self.driver = driver

    def t_shirt_page(self):
        t_shirt_btn = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
        self.driver.implicitly_wait(3)
        t_shirt_btn.click()

        quickview = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div')
        self.driver.implicitly_wait(3)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(quickview).perform()
            time.sleep(4)

            blue_color = self.driver.find_element(By.ID, 'color_2')
            blue_color.click()
            time.sleep(2)

        except:
            print('Mouse Hover Action Failed.')

        add_to_cart = self.driver.find_element(By.XPATH, '//*[@id="add_to_cart"]/button')
        self.driver.implicitly_wait(3)
        add_to_cart.click()
        time.sleep(4)

        verified_message = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
        time.sleep(2)

        display = verified_message.is_displayed()
        if display is True:
            print('Product successfully added to your shopping cart')
        else:
            print('Product not added')

        time.sleep(2)
        proceed_to_checkout = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
        proceed_to_checkout.click()
        time.sleep(2)
