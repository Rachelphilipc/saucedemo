import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
class SauceDemoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.get("https://www.saucedemo.com")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_valid_credentials(self):
        username = "standard_user"
        password = "secret_sauce"

        self.login(username, password)

        # Verify successful login
        self.assertIn("inventory.html", self.driver.current_url)

    def test_login_invalid_credentials(self):
        username = "invalid_user"
        password = "invalid_password"

        self.login(username, password)

        # Verify login failed
        error_message = self.driver.find_element_by_css_selector("[data-test='error']").text
        self.assertEqual(error_message, "Epic sadface: Username and password do not match any user in this service")

    def test_navigate_to_products_page(self):
        username = "standard_user"
        password = "secret_sauce"

        self.login(username, password)

        # Navigate to Products page
        products_link = self.driver.find_element_by_link_text("Products")
        products_link.click()

        # Verify Products page is displayed
        self.assertIn("inventory.html", self.driver.current_url)

    def test_add_product_to_cart(self):
        username = "standard_user"
        password = "secret_sauce"

        self.login(username, password)

        # Add product to cart
        add_to_cart_button = self.driver.find_element_by_css_selector("[data-test='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()

        # Verify product is added to cart
        cart_item_count = self.driver.find_element_by_css_selector(".shopping_cart_badge").text
        self.assertEqual(cart_item_count, "1")

    @unittest.skip("Skipping logout test for now")
    def test_logout_from_application(self):
        username = "standard_user"
        password = "secret_sauce"

        self.login(username, password)

        # Logout from application
        menu_button = self.driver.find_element_by_css_selector("#react-burger-menu-btn")
        menu_button.click()
        logout_link = self.driver.find_element_by_id("logout_sidebar_link")
        logout_link.click()

        # Verify logout
        self.assertIn("index.html", self.driver.current_url)

    def login(self, username, password):
        username_field = self.driver.find_element_by_id("user-name")
        password_field = self.driver.find_element_by_id("password###KOMALI")
        login_button = self.driver.find_element_by_css_selector("[type='submit']")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

if __name__ == '__main__':
    # Run the tests
    suite = unittest.TestLoader().loadTestsFromTestCase(SauceDemoTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Count the number of passed, failed, and skipped tests
    passed = result.testsRun - len(result.errors) - len(result.failures)
    failed = len(result.errors) + len(result.failures)
    skipped = len(result.skipped)

    # Print the result in the desired format
    print(f"passed {passed}, failed {failed}, skipped {skipped}")
