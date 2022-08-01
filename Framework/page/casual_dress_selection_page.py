import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class DressSelectionPage:

    def __init__(self, driver):
        self.driver = driver

    def dress_selection(self):
        dresses = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
        self.driver.implicitly_wait(3)

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(dresses).perform()
            time.sleep(3)

            casual_dresses = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/ul/li[1]/a')
            casual_dresses.click()
            time.sleep(2)

        except:
            print('Mouse Hover Action Failed.')

        quickview = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div/div[1]/div/a[2]/span')
        self.driver.implicitly_wait(3)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(quickview).perform()
            time.sleep(4)

            add_to_cart = self.driver.find_element(By.LINK_TEXT, 'Add to cart')
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
            continue_shopping = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span')
            continue_shopping.click()
            time.sleep(3)

        except:
            print('Mouse Hover Action Failed.')
