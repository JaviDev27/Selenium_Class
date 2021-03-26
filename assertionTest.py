import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
# Para validadr la presencia de un elemento.
from selenium.common.exceptions import NoSuchElementException
# Sub modulo by para llamar a las excepciones que queremos llamar
from selenium.webdriver.common.by import By


class Assertion_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    # identificamos el campo de busqueda
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    """ Valida presensia de elementos """

    def test_languaje_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    """ Este metodo permite identificar cuando existe un 
    elemento de acuerdo a sus parámetros
    how es el tipo de selector
    what el valor que tiene"""

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)
