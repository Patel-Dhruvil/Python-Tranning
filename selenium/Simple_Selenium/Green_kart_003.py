import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'search-keyword']").send_keys("ber")

#driver.find_element(by=By.CSS_SELECTOR,value="button[class= 'search-button']").click()
time.sleep(1)
product = (driver.find_elements(by=By.CSS_SELECTOR,value="div[class = 'product']"))

product_name = (driver.find_elements(by=By.CSS_SELECTOR,value="h4[class = 'product-name']"))
for i in product_name:
    print(i.text)

time.sleep(1)
select_product = (driver.find_elements(by=By.CSS_SELECTOR,value="div[class = 'product-action']"))
for i in select_product:
    i.click()

driver.find_element(by=By.CSS_SELECTOR,value="a[class = 'cart-icon']").click()
driver.find_element(by=By.CSS_SELECTOR,value="div[class = 'action-block']").click()

time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'promoCode']").send_keys("rahulshettyacademy")
driver.find_element(by=By.CSS_SELECTOR,value="button[class = 'promoBtn']").click()
time.sleep(8)
driver.find_element(by=By.XPATH,value="//button[text() = 'Place Order']").click()
#driver.find_element(by=By.TAG_NAME,value="Select").click()
driver.find_element(by=By.CSS_SELECTOR,value="option[value = 'India']").click()

driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'chkAgree']").click()
time.sleep(1)
driver.find_element(by=By.XPATH,value="//button[text() = 'Proceed']").click()


time.sleep(8)
driver.close()
driver.quit()