import unittest
from selenium import webdriver

# Permite hacer referencia a sus elementos por sus selectores, no para identificarlso sino para interactuar
from selenium.webdriver.common.by import By

# Permite hacer uso de espected condicion junto con las eperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

# esperas explicitas
from selenium.webdriver.support import expected_conditions as EC


class DinamicControls(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dinamic_control(self):
        driver = self.driver

        REMOVE_button = driver.find_element_by_xpath(
            '//*[@id="checkbox-example"]/button').click()

        checkbox = WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="checkbox"]/input')))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
