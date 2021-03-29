import unittest
from selenium import webdriver


class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input("How many elements will you add?: "))
        elements_removed = int(input("How many elements will you remove?: "))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/button')

        driver.implicitly_wait(3)

        for i in range(elements_added):
            driver.implicitly_wait(2)
            add_button.click()

        for i in range(elements_removed):
            try:
                deleted_button = driver.find_element_by_xpath(
                    '//*[@id="elements"]/button')
                deleted_button.click()
                driver.implicitly_wait(2)
            except:
                print('Your try to deleted more elements that exist')
                break

        if total_elements > 0:
            print(f'there are {total_elements} elements on screen')
        else:
            print(f'there are 0 elements on screen')

        driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
