from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    login_link = (By.CSS_SELECTOR, "a[class = 'ico-login']")          # under <a> tag
    apparel_and_shoes_link = (By.CSS_SELECTOR, "a[href = '/apparel-shoes']")    # under <a> tag
    user_profile_link = (By.CSS_SELECTOR, "a[class = 'account']")   # under <a> tag
    shopping_cart_link = (By.CSS_SELECTOR, "a[class = 'ico-cart']")  # under <a> tag
    logout_link = (By.CSS_SELECTOR, "a[class = 'ico-logout']")   # under <a> tag
    home_image_link = (By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[1]/a/img")



    def loginPageLink(self):
        return self.driver.find_element(*HomePage.login_link)

    def apparelAndShoes(self):
        return self.driver.find_element(*HomePage.apparel_and_shoes_link)

    def userProfile(self):
        return self.driver.find_element(*HomePage.user_profile_link)

    def shoppingCart(self):
        return self.driver.find_element(*HomePage.shopping_cart_link)

    def logout(self):
        return self.driver.find_element(*HomePage.logout_link)

    def homeImageLink(self):
        return self.driver.find_element(*HomePage.home_image_link)


