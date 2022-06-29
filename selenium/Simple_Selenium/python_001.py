import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("https://google.co.in")
driver.maximize_window()
time.sleep(1)

driver.find_element(by = By.CSS_SELECTOR, value="input[class = 'gLFyf gsfi']").send_keys("www.einfochips.com/")
driver.find_element(by = By.XPATH,value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()
time.sleep(2)
driver.find_element(by=By.PARTIAL_LINK_TEXT,value="https://www.einfochips.com").click()


time.sleep(10)
driver.close()
