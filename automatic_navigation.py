import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# Para validadr la presencia de un elemento.
from selenium.common.exceptions import NoSuchElementException
# Sub modulo by para llamar a las excepciones que queremos llamar
from selenium.webdriver.common.by import By


class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get('https://www.google.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_brouser_nav(self):
        driver = self.driver
        search_fiel = driver.find_element_by_name('q')
        search_fiel.clear()
        search_fiel.send_keys('Platzi')
        search_fiel.submit()

        driver.back()
        driver.implicitly_wait(5)
        driver.forward()
        driver.implicitly_wait(5)
        driver.refresh()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
