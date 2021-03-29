import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# Permite hacer referencia a sus elementos por sus selectores, no para identificarlso sino para interactuar
from selenium.webdriver.common.by import By

# Permite hacer uso de espected condicion junto con las eperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

# esperas explicitas
from selenium.webdriver.support import expected_conditions as EC


class ExplicityWaitTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    def test_account_link(self):
        # busco el elemento por el id y verifico si existen 3 elementos
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id(
            'select-language').get_attribute('length') == '3')

        # hace referencia al enlace donde estan las cuentas y espera hasta que exista la vista mandas
        ''' Parametros en located como una tupla '''
        account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))

        account.click()

    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        # espera hasta que se cumpla la condición. verifica si un elemento esta visibles
        my_account = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))

        my_account.click()

        # que pueda ser clickeable
        create_account_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_btn.click()

        # si esta en la pagina correcpondiente
        WebDriverWait(self.driver, 10).until(
            EC.title_contains('Create New Customer Account'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
