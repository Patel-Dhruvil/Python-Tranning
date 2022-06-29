import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("https://demo.guru99.com/test/")
driver.maximize_window()
print("start")
driver.find_element(by=By.CSS_SELECTOR,value="input[name = 'bdaytime']").send_keys("02/02/2000 02:02:02")
print(driver.find_element(by=By.CSS_SELECTOR,value="input[name = 'bdaytime']").text)
print("stop")
time.sleep(5)
driver.close()
driver.quit()


