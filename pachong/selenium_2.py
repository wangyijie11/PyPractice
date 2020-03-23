import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    """python官网查询类

    attributes:


    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        """查询方法

        args:

        returns:

        raises:

        """
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No result found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()