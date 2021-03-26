import unittest
from selenium import webdriver
''' Para seleccionar en una lista '''
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_slect_language(self):
        exp_options = ['English', 'French', 'German']  # lista de opciones
        act_options = []  # Contiene las opciones

        select_language = Select(
            self.driver.find_element_by_id('select-language'))  # seleccionno el dropdown

        self.assertEqual(len(select_language.options),
                         3)  # verifico si existen 3

        for option in select_language.options:
            act_options.append(option.text)

        # verifican si son identicas
        self.assertListEqual(act_options, exp_options)

        # selecciona la primera
        self.assertEqual('English', select_language.first_selected_option.text)
        select_language.select_by_visible_text('German')

        # verifica si esta en aleman verifica en el url
        self.assertTrue('store=german' in self.driver.current_url)

        self.driver.implicitly_wait(5)

        select_language = Select(
            self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
