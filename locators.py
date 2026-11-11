from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


def test_by_id(browser):
   browser.get('https://www.saucedemo.com/')


# Основные локаторы
   username_field = browser.find_element(By.ID, "user-name")  # по id
   username_field.send_keys('standard_user')
   password_field = browser.find_element(By.NAME, "password") # по name
   password_field.send_keys('secret_sauce')
   login_button = browser.find_element(By.CLASS_NAME, 'submit-button')  # по CLASS_NAME
   login_button.send_keys(Keys.ENTER)
   footer= browser.find_element(By.TAG_NAME, 'footer')  # по тегу
   full_link_text_backpack = browser.find_element(By.LINK_TEXT, 'Sauce Labs Backpack')  # полному совпадению текста ссылки
   partial_link_text_backpack = browser.find_element(By.PARTIAL_LINK_TEXT, 'Backpack')  # частичному совпадению текста ссылки


# XPath
   backpack_price = browser.find_element(By.XPATH, '//div[@class = "inventory_item_price"]')  # по атрибуту
   logo = browser.find_element(By.XPATH, '//div[text() = "Swag Labs"]')  # по тексту
   onesie_img = browser.find_element(By.XPATH, '//img[contains(@alt, "Onesie")]')  # по частичному совпадению атрибута
   t_shirt = browser.find_element(By.XPATH, '//div[contains(text(), "Red")]')  # по частичному совпадению текста

# По осям XPath
   browser.find_element(By.XPATH, '//a[@data-test="item-1-title-link"]/ancestor::div[1]')  # по ancestor
   browser.find_elements(By.XPATH, '//div[@data-test="inventory-item"]//descendant::img')  # по descendant
   browser.find_elements(By.XPATH,'//div[@data-test="inventory-item"][1]/following::*')  # по following
   browser.find_element(By.XPATH,'//div[contains(text(), "Swag Labs")]/parent::header')  # по parent
   browser.find_elements(By.XPATH,'//div[contains(text(), "Swag Labs")]/preceding::*')  # по preceding


   backpack_add_to_cart = browser.find_element(By.XPATH, '//button[text()="Add to cart" and @id="add-to-cart-sauce-labs-backpack"]')  # c условием and


# CSS-селекторы
   sorting = browser.find_element(By.CSS_SELECTOR, '.product_sort_container')  # по одному классу
   add_to_cart_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn_primary')  # по двум классам
   burger_menu = browser.find_element(By.CSS_SELECTOR, '.primary_header .bm-burger-button')  # по классу вложенному в др класс
   shopping_cart = browser.find_element(By.CSS_SELECTOR, '#shopping_cart_container')  # по id
   filter_container = browser.find_element(By.CSS_SELECTOR, 'select')  # по тегу
   item_description = browser.find_element(By.CSS_SELECTOR, 'div.inventory_item_desc')  # по тегу и классу
   img_fleece_jacket = browser.find_element(By.CSS_SELECTOR, 'img[alt = "Sauce Labs Fleece Jacket"]')  # по значению атрибута
   img_bolt_t_shirt_contains = browser.find_element(By.CSS_SELECTOR, 'img[alt ~= "Bolt"]') # по ~ (атрибут содержит в себе)
#   img_bolt_t_shirt_starts_with = browser.find_element(By.CSS_SELECTOR, 'img[alt|= "Sauce"]') # по | (атрибут содержит тире, но я такого не нашла. Не уверена, что вообще правильно поняла)
   img_bike_lights_begins_with = browser.find_element(By.CSS_SELECTOR, 'img[alt^="Sauce"]') # по ^ (атрибут начинается с ...)
   img_bike_lights_ends_with = browser.find_element(By.CSS_SELECTOR, 'img[alt $= "Light"]') # по ^ (атрибут заканчивается на ...)
   bike_lights_contains = browser.find_elements(By.CSS_SELECTOR, 'a[aria-label*="T-Shirt"]') # ищу список элементов по * (атрибут содержит в себе)
