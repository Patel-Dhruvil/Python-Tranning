from selenium.webdriver.common.by import By

global paymentMethodName
global shippingMethodName
class Checkout:
    def __init__(self, driver):
        self.driver = driver

    billing_address_continue = (By.XPATH, "//div[@id = 'billing-buttons-container']/input[@title = 'Continue']")
    shipping_address_continue = (By.XPATH, "//div[@id = 'shipping-buttons-container']/input[@title = 'Continue']")

    shipping_method_continue = (By.XPATH, "//div[@id = 'shipping-method-buttons-container']/input[@value = 'Continue']")
    get_payment_method_name = (By.XPATH, "//*[@id = 'checkout-payment-method-load']/div/div/ul/li[1]/div/div[2]/label")
    payment_method_continue = (By.XPATH, "//*[@id='payment-method-buttons-container']/input[@value = 'Continue']")
    payment_information_continue = (By.XPATH, "//*[@id='payment-info-buttons-container']/input[@value = 'Continue']")
    confirm_order_button = (By.XPATH, "//*[@id='confirm-order-buttons-container']/input[@value = 'Confirm']")
    order_continue_button = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/div[2]/input")
    order_number_text = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/ul/li[1]")


    def billingAddressContinue(self):
        return self.driver.find_element(*Checkout.billing_address_continue)

    def shippingAddressContinue(self):
        return self.driver.find_element(*Checkout.shipping_address_continue)

    def selectShippingMethod(self, option):
        select_shipping_method = (By.XPATH, f"//*[@id='shippingoption_{option}']")
        return self.driver.find_element(*select_shipping_method)

    def getShippingMethodName(self, option):
        get_shipping_method_name = (By.CSS_SELECTOR, f"label[for = 'shippingoption_{option}']")
        return self.driver.find_element(*get_shipping_method_name)

    def shippingMethodContinue(self):
        return self.driver.find_element(*Checkout.shipping_method_continue)

    def selectPaymentMethod(self, option):
        select_payment_method = (By.XPATH, f"//*[@id='paymentmethod_{option}']")
        return self.driver.find_element(*select_payment_method)

    def getPaymentMethodName(self):
        return self.driver.find_element(*Checkout.get_payment_method_name)

    def paymentMethodContinue(self):
        return self.driver.find_element(*Checkout.payment_method_continue)

    def paymentInformationContinue(self):
        return self.driver.find_element(*Checkout.payment_information_continue)

    def confirmOrderButton(self):
        return self.driver.find_element(*Checkout.confirm_order_button)

    def orderContinueButton(self):
        return self.driver.find_element(*Checkout.order_continue_button)

    def orderNumberText(self):
        return self.driver. find_element(*Checkout.order_number_text)
