from selenium.webdriver.common.by import By


class UserProfile:

    def __init__(self,driver):
        self.driver = driver

    order_link_click = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[1]/div/div[2]/ul/li[3]/a")
    confirm_order_number = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div/div[1]/div[1]/strong")

    def orderLinkClick(self):
        return self.driver.find_element(*UserProfile.order_link_click)

    def confirmOrderNumber(self):
        return self.driver.find_element(*UserProfile.confirm_order_number)