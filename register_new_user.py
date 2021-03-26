import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_btn = driver.find_element_by_xpath(
            '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(create_account_btn.is_displayed()
                        and create_account_btn.is_enabled())
        create_account_btn.click()

        # verifico si estoy en la pagina de crear usuario
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        new_letter_subscription = driver.find_element_by_id('is_subscribed')
        # nunca usaes datos reales
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath(
            '//*[@id="form-validate"]/div[2]/button')

        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and new_letter_subscription.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and submit_button.is_enabled())

        first_name.send_keys('Test1')
        driver.implicitly_wait(10)
        middle_name.send_keys('Test1')
        driver.implicitly_wait(10)
        last_name.send_keys('Test1')
        driver.implicitly_wait(10)
        email_address.send_keys('Test1@test.com')
        driver.implicitly_wait(10)
        password.send_keys('Test1')
        driver.implicitly_wait(10)
        confirm_password.send_keys('Test1')
        driver.implicitly_wait(10)
        submit_button.click()
        driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
