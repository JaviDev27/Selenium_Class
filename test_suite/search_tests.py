import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class Home_Page_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()

    def test_search_text_field(self):
        # Busca su elemento por el ID
        self.search_field = self.driver.find_element_by_id('search')

    def test_search_text_field_by_name(self):
        self.search_field = self.driver.find_element_by_name('q')

    def test_search_text_field_by_clase(self):
        self.search_field = self.driver.find_element_by_class_name(
            'input-text')

    def test_search_button_enable(self):
        self.search_button = self.driver.find_element_by_class_name('button')

    # Se puede contar el numero de elementos usando el tag
    def test_count_of_promo_banner_imagen(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners))

    """
    El xpath nos permite identificar elementos que no estan implicitos
    """

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath(
            '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

    # se lo puede identificar por el selector de css
    def test_shopping_cart(self):
        shoppig_icon = self.driver.find_element_by_css_selector(
            'div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
