import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class SauceDemoLoginTests(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        # Add any necessary options here
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(10)  # Example implicit wait
        
    def tearDown(self):
        self.driver.quit()
