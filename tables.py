import unittest
from selenium import webdriver

# Permite hacer referencia a sus elementos por sus selectores, no para identificarlso sino para interactuar
from selenium.webdriver.common.by import By

# Permite hacer uso de espected condicion junto con las eperas explicitas
from selenium.webdriver.support.ui import WebDriverWait

# esperas explicitas
from selenium.webdriver.support import expected_conditions as EC


class Tables(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.driver.get('http://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(5)]

        print(table_data)

        for row in range(len(table_data)):
            for col in range(6):

                if row == 0:
                    header = driver.find_element_by_xpath(
                        f'//*[@id="table1"]/thead/tr/th[{col+1}]/span')
                    print(col)
                    table_data[row].append(header.text)
                else:
                    row_data = driver.find_element_by_xpath(
                        f'//*[@id="table1"]/tbody/tr[{row}]/td[{col+1}]')
                    table_data[row].append(row_data.text)

        for data in table_data:
            print(data)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
