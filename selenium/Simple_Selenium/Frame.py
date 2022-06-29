import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(3)


driver.switch_to.frame("mce_0_ifr")
driver.find_element(by=By.CSS_SELECTOR,value=".mce-content-body").clear()

driver.find_element(by=By.CSS_SELECTOR,value="body[id = 'tinymce']").send_keys("Dhruvil")

# wait = WebDriverWait(driver, 8)
# wait.until(expected_conditions.)
time.sleep(5)
driver.close()
driver.quit()