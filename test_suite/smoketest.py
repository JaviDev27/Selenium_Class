from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertionTest import Assertion_Test
from searchTest import SearchTest

''' Aqui 
esta llamndo a todas las pruebas '''
assertionTest = TestLoader().loadTestsFromTestCase(Assertion_Test)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

''' Contruyes la suit
pasas las pruebas a la suite '''
smoke_test = TestSuite([assertionTest, search_test])

''' Defines el nombre del report '''
kwargs = {
    "output": "smoke_report"
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
