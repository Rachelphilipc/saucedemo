from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest
import time

options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
class SauceDemoLoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.saucedemo.com")

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.assertEqual(self.driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_invalid_username(self):
        self.driver.find_element(By.ID, "user-name").send_keys("invalid_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//h3").text
        self.assertIn("do not match", error_message)

    def test_invalid_password(self):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("wrong_password")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//h3").text
        self.assertIn("do not match", error_message)

    def test_empty_username(self):
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//h3").text
        self.assertIn("required", error_message)

    def test_skip_test_no_internet(self):
        # This would typically be handled externally, but for demonstration:
        self.skipTest("No internet connection - skipping the test.")

if __name__ == "__main__":
    unittest.main()
    time.sleep(5)
