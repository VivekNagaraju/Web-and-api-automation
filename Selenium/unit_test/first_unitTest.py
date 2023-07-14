import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrangeHRM(unittest.TestCase):


    def test_navigation(self):
        opts=webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.assertEqual()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()