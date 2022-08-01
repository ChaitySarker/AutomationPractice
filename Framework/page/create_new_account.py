import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def create_account(self, firstname, lastname, password, company, Address, city, zip, addInfo, homephone, mobilephone,
                       refaddress):

        # Select Title
        title = self.driver.find_element(By.ID, 'id_gender2')
        title_status = title.is_selected()

        if not title_status:
            title.click()
        time.sleep(2)

        first_name = self.driver.find_element(By.ID, 'customer_firstname')
        first_name.send_keys(firstname)

        last_name = self.driver.find_element(By.ID, 'customer_lastname')
        last_name.send_keys(lastname)

        password_field = self.driver.find_element(By.ID, 'passwd')
        password_field.send_keys(password)

        day = self.driver.find_element(By.ID, 'days')
        sel = Select(day)
        sel.select_by_value('1')

        month = self.driver.find_element(By.ID, 'months')
        sel = Select(month)
        sel.select_by_value('1')

        year_field = self.driver.find_element(By.ID, 'years')
        sel = Select(year_field)
        sel.select_by_value('1994')
        time.sleep(2)

        company_field = self.driver.find_element(By.ID, 'company')
        company_field.send_keys(company)

        address_field = self.driver.find_element(By.ID, 'address1')
        address_field.send_keys(Address)

        city_field = self.driver.find_element(By.ID, 'city')
        city_field.send_keys(city)

        state_field = self.driver.find_element(By.ID, 'id_state')
        sel = Select(state_field)
        sel.select_by_value('9')
        time.sleep(2)

        zip_postal_code = self.driver.find_element(By.ID, 'postcode')
        zip_postal_code.send_keys(zip)

        country = self.driver.find_element(By.ID, 'id_country')
        sel = Select(country)
        sel.select_by_value('21')
        time.sleep(2)

        additional_info = self.driver.find_element(By.ID, 'other')
        additional_info.send_keys(addInfo)

        home_phone = self.driver.find_element(By.ID, 'phone')
        home_phone.send_keys(homephone)

        mobile_phone = self.driver.find_element(By.ID, 'phone_mobile')
        mobile_phone.send_keys(mobilephone)

        alias = self.driver.find_element(By.ID, 'alias')
        alias.send_keys(refaddress)
        time.sleep(2)

        register = self.driver.find_element(By.ID, 'submitAccount')
        register.click()
        time.sleep(5)
