import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SaucedemoTests(unittest.TestCase):

    def setUp(self):
        # Set up WebDriver
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Implicit wait for 10 seconds

    def tearDown(self):
        # Clean up
        self.driver.quit()

    def test_login_valid(self):
        # Test login with valid credentials
        self.driver.get("https://www.saucedemo.com/")
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        # Assert user navigates to inventory page
        self.assertTrue("inventory.html" in self.driver.current_url)

    def test_login_invalid(self):
        # Test login with invalid credentials
        self.driver.get("https://www.saucedemo.com/")
        username_field = self.driver.find_element(By.ID, "user-name")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")
        username_field.send_keys("locked_out_user")
        password_field.send_keys("secret_sauce")
        login_button.click()
        # Assert error message is displayed
        error_message = self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        self.assertEqual(error_message.text, "Epic sadface: Sorry, this user has been locked out.")

    def test_add_to_cart(self):
        # Test adding item to cart
        self.driver.get("https://www.saucedemo.com/inventory.html")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='ADD TO CART']")
        add_to_cart_button.click()
        # Assert cart count increases
        cart_count = self.driver.find_element(By.CSS_SELECTOR, "span.shopping_cart_badge")
        self.assertEqual(cart_count.text, "1")

    def test_sort_products(self):
        # Test sorting products
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sort_dropdown = self.driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        option_price_low_to_high = self.driver.find_element(By.XPATH, "//option[text()='Price (low to high)']")
        option_price_low_to_high.click()
        # Assert products are sorted correctly
        product_prices = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
        prices = [float(price.text.replace('$', '')) for price in product_prices]
        self.assertEqual(prices, sorted(prices))

    def test_logout(self):
        # Test logout functionality
        self.driver.get("https://www.saucedemo.com/inventory.html")
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        logout_button = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout_button.click()
        # Assert user navigates back to login page
        self.assertTrue("index.html" in self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
