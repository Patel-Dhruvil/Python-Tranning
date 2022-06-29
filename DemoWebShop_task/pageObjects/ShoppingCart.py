from selenium.webdriver.common.by import By


class ShoppingCart:
    def __init__(self, driver):
        self.driver = driver

    get_coupon_code = (By.CSS_SELECTOR, "input[name = 'discountcouponcode']")
    apply_coupon_code = (By.CSS_SELECTOR, "input[name = 'applydiscountcouponcode']")
    agree_terms = (By.XPATH, "//*[@id='termsofservice']")
    checkout_button = (By.XPATH, "//*[@id='checkout']")
    coupon_code_message = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div[1]/div/div[1]/div[4]")

    def getCouponCode(self):
        return self.driver.find_element(*ShoppingCart.get_coupon_code)

    def applyCouponCodeButton(self):
        return self.driver.find_element(*ShoppingCart.apply_coupon_code)

    def couponCodeMessage(self):
        return self.driver.find_element(*ShoppingCart.coupon_code_message)

    def agreeTerms(self):
        return self.driver.find_element(*ShoppingCart.agree_terms)

    def checkoutButton(self):
        return self.driver.find_element(*ShoppingCart.checkout_button)

