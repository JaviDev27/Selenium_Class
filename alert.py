import unittest
from selenium import webdriver
''' Para seleccionar en una lista '''
from selenium.webdriver.support.ui import Select


class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys("tee")
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()

        driver.find_element_by_link_text('Clear All').click()
        # Aqui dispar el alñert
        alert = driver.switch_to_alert()  # cambia el foco a la alaerta
        alert_text = alert.text  # estraemos el texto que nos muestra

        self.assertEqual('Are you sure you would like to remove all products from your comparison?',
                         alert_text)  # valida si son identicos

        alert.accept()  # aqui aceptas la alerta

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
