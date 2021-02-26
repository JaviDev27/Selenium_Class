import unittest
# Ayuda a orquestar cada prueba con los reportes
from pyunitreport import HTMLTestRunner
from selenium import webdriver

# Tenemos una clase


class Hello_World(unittest.TestCase):
    # prepara el entorno de la prueba
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='./chromedriver.exe')  # llamo al driver de chrome
        driver = cls.driver
        driver.implicitly_wait(10)

    # caso de la prueb para automatizar

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    # otras actividades para finalizar la prueba generalmente es cerrar laventana del navegador
    # despues de cada p`rueba

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reportes', report_name='hello_world_report'))
