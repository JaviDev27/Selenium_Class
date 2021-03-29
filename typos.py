import unittest
from selenium import webdriver

# Permite hacer referencia a sus elementos por sus selectores, no para identificarlso sino para interactuar
from selenium.webdriver.common.by import By

# Permite hacer uso de espected condicion junto con las eperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

# esperas explicitas
from selenium.webdriver.support import expected_conditions as EC


class Typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text('Typos').click()

    def test_typos(self):
        driver = self.driver

        paragrhap_to_check = driver.find_element_by_css_selector(
            '#content > div > p:nth-child(3)')
        text_to_check = paragrhap_to_check.text

        print(text_to_check)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:

            paragrhap_to_check = driver.find_element_by_css_selector(
                '#content > div > p:nth-child(3)')
            text_to_check = paragrhap_to_check.text
            driver.refresh()
            tries += 1

        print(f'{tries} tries')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
