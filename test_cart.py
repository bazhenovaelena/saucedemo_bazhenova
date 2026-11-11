from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

def test_by_id(browser):
   browser.get('https://www.saucedemo.com/')
   username_field = browser.find_element(By.ID, "user-name")
   username_field.send_keys('standard_user')
   password_field = browser.find_element(By.NAME, "password")
   password_field.send_keys('secret_sauce')
   login_button = browser.find_element(By.CLASS_NAME, 'submit-button')
   login_button.send_keys(Keys.ENTER)

   bike_lights_add_to_cart = browser.find_element(By.XPATH, '//button[@name="add-to-cart-sauce-labs-bike-light"]')
   bike_lights_add_to_cart.click()
   cart_btn = browser.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
   cart_btn.click()

   bike_lights_item_name = browser.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
   text = bike_lights_item_name.text

   assert text == "Sauce Labs Bike Light"

   price = browser.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
   price_text = price.text
   assert price_text== "$9.99"




