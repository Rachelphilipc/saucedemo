import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class SauceDemoLoginTests(unittest.TestCase):
    
    def setUp(self):
        options = Options()
        # Add any necessary options here
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(10)  # Example implicit wait
        self.driver.get("https://www.saucedemo.com")
        
    def tearDown(self):
        self.driver.quit()
    
