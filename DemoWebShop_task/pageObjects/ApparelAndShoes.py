import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from pageObjects.HomePage import HomePage


class ApparelAndShoes:
    def __init__(self, driver):
        self.driver = driver


    def orderItem(self, product_id, product_quantity):
        homePage = HomePage(self.driver)
        self.driver.find_element(by = By.XPATH, value = f"//div[@data-productid='{product_id}']/div/a").click()
        time.sleep(2)
        self.driver.find_element(by=By.CSS_SELECTOR, value= f"input[id = 'addtocart_{product_id}_EnteredQuantity']").clear()
        self.driver.find_element(by=By.CSS_SELECTOR, value= f"input[id = 'addtocart_{product_id}_EnteredQuantity']").send_keys(f"{product_quantity}")
        time.sleep(2)
        add_to_cart_button = (By.CSS_SELECTOR, f"input[id = 'add-to-cart-button-{product_id}']")

        return self.driver.find_element(*add_to_cart_button)
