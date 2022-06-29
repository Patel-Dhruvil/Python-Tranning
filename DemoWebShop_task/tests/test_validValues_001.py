import time

import pytest
from selenium.webdriver.common.by import By

from TestData.GetData import HomePageData
from pageObjects.ApparelAndShoes import ApparelAndShoes
from pageObjects.Checkout import Checkout
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.ShoppingCart import ShoppingCart
from pageObjects.UserProfile import UserProfile
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_login(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)

        log.info("Getting all the card titles")

        homePage.loginPageLink().click()
        time.sleep(6)
        loginPage.getEmail().send_keys(getData["Email"])
        loginPage.getPassword().send_keys(getData["Password"])
        time.sleep(1)
        loginPage.clickLogin().click()
        assert self.driver.find_element(by=By.CSS_SELECTOR, value="a[class = 'ico-logout']").text == "Log out", "Login Failed."

    def test_navigate_to_blue_jeans(self,getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        apparelAndShoes = ApparelAndShoes(self.driver)

        homePage.apparelAndShoes().click()
        time.sleep(7)
        pid=getData["ProductId"]
        pq=getData["Quantity"]
        apparelAndShoes.orderItem(pid,pq).click()
        time.sleep(5)

        homePage.shoppingCart().click()
        time.sleep(5)

    def test_apply_coupon_code(self,getData):

        shoppingCartPage = ShoppingCart(self.driver)
        shoppingCartPage.getCouponCode().send_keys(getData["CouponCode"])
        shoppingCartPage.applyCouponCodeButton().click()
        time.sleep(3)
        assert shoppingCartPage.couponCodeMessage().text == "The coupon code was applied", "Coupon did not applied successfully."

        shoppingCartPage.agreeTerms().click()
        time.sleep(2)
        shoppingCartPage.checkoutButton().click()

    def test_checkout(self,getData):

        checkout = Checkout(self.driver)
        homePage = HomePage(self.driver)
        userProfile = UserProfile(self.driver)
        time.sleep(2)
        checkout.billingAddressContinue().click()
        time.sleep(2)
        checkout.shippingAddressContinue().click()
        time.sleep(2)
        checkout.selectShippingMethod(getData["shipping_method_id"]).click()
        shippingMethodName = checkout.getShippingMethodName(getData["shipping_method_id"]).text    # storing name of shipping method in a variable
        shippingMethodName = shippingMethodName.split()
        time.sleep(2)
        checkout.shippingMethodContinue().click()
        time.sleep(2)
        checkout.selectPaymentMethod(getData["payment_method_id"]).click()
        time.sleep(2)
        checkout.paymentMethodContinue().click()
        time.sleep(2)
        checkout.paymentInformationContinue().click()
        time.sleep(2)
        checkout.confirmOrderButton().click()      #final confirm order button gets click here
        time.sleep(5)
        orderNumber = checkout.orderNumberText().text
        checkout.orderContinueButton().click()

        orderNumber = orderNumber.split()
        time.sleep(1)
        homePage.userProfile().click()
        time.sleep(2)
        userProfile.orderLinkClick().click()
        time.sleep(2)
        confirm_orderNumber = userProfile.confirmOrderNumber().text
        confirm_orderNumber = confirm_orderNumber.split()
        assert confirm_orderNumber[-1] == orderNumber[-1], "Order Number is matched."


    @pytest.fixture(params=HomePageData.getTestData("DiscountTypeFlat_002"))  # Parameterizing Tests using
    # data fixture with multiple Data Sets
    def getData(self, request):  # request return data - function with return value
        return request.param

