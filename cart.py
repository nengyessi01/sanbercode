import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AddtoCart(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        # webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url = "https://www.saucedemo.com/"

    def test_add_to_cart(self): #step 1
        driver = self.browser #buka web browser
        driver.get(self.url) # buka situs
        driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys("standard_user") # isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        driver.find_element(By.CLASS_NAME, "btn_action").click()
        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('Products', response_data)

        driver.find_element (By.XPATH,"/html//button[@id='add-to-cart-sauce-labs-backpack']").click()
        cart = driver.find_element (By.CLASS_NAME,"shopping_cart_badge").text
        self.assertEqual (cart, "1")
        driver.find_element (By.CLASS_NAME,"shopping_cart_badge").click()
        url = driver.current_url
        self.assertIn ('/cart.html',url)
        driver.find_element(By.CLASS_NAME,"inventory_item_name")
        

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
