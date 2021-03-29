import unittest
from selenium import webdriver


class DinamicElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text('Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver
        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()

            """SE EMPIEZA A CONTAR Y FRESESCAR LA PANTALAL HASTA ENCONTRAR EL ELEMENTO GELLERY
            """

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(
                        f'//*[@id="content"]/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except Exception as ex:
                    print(f'option number {i+1} is not found')
                    tries += 1
                    driver.refresh()

        print(f'finish in {tries}')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
