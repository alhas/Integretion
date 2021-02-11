import unittest

from selenium import webdriver

PATH = "/usr/bin/chromedriver"

class TestViews(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=PATH)
        cls.driver.get("http://0.0.0.0:8000/")

    def test_buttons(self):
        self.driver.find_element_by_name("one").click()
        self.driver.find_element_by_name("two").click()
        self.driver.find_element_by_name("three").click()
        self.driver.find_element_by_name("times").click()
        self.driver.find_element_by_name("three").click()
        self.driver.find_element_by_id("result").click()
        actualvalue = self.driver.find_element_by_id("display").get_attribute("value")
        assert actualvalue == "369"

    def test_inputs(self):
        self.driver.find_element_by_id("clear").click()
        self.driver.find_element_by_name("display").send_keys(1234 * 123)
        self.driver.find_element_by_id("result").click()
        actualvalue = self.driver.find_element_by_id("display").get_attribute("value")
        assert actualvalue == "151782"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
