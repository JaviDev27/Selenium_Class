import unittest
from pyunitreport import HTMLTestRunner
from ddt import ddt, data, unpack
from selenium import webdriver
import csv


def get_data(file_name):
    rows = []

    data_file = open(file_name, 'r')
    """ se encarga de leer el archivo """
    reader = csv.reader(data_file)
    """ pasa a la siguiente dila de datos """
    next(reader, None)

    for row in reader:
        rows.append(row)

    return rows

# colocas el decorador


@ddt
class search_ddt_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(30)

    # decorador con tuplas como parametro de lo
    # que se esta buscando y de cuantos va a encontrar
    @data(*get_data('testdata.csv'))
    # decorador para desempacar las tuplas
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        """Busqueda 

        Args:
            search_value (string): el valor buscado 
            expected_count ([type]): numero que se espera encontrar
        """

        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        # buscamos los productos

        products = driver.find_elements_by_xpath(
            '//h2[@class="product-name"]/a')

        expected_count = int(expected_count)

        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)

        print(f'found {len(products)} products')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
