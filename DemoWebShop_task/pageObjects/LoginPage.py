from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    get_email = (By.CSS_SELECTOR, "input[id = 'Email']")
    get_password = (By.CSS_SELECTOR, "input[id = 'Password']")
    click_login = (By.XPATH, "//div[@class = 'buttons']/input[@value = 'Log in']")


    def getEmail(self):
        return self.driver.find_element(*LoginPage.get_email)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.get_password)

    def clickLogin(self):
        return self.driver.find_element(*LoginPage.click_login)

