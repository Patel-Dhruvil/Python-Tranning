import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("http://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
time.sleep(1)
driver.execute_script("window.scrollTo(0,420)")

driver.find_element(by=By.CSS_SELECTOR,value="input[name ='name']").send_keys("Dhruvi Patel")
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[name ='email']").send_keys("Dhruvi.Patel@mail.com")
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'form-control']").send_keys("12345678")
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'form-check-input']").click()
time.sleep(1)

dropdown = Select(driver.find_element(by=By.CSS_SELECTOR,value="select[class = 'form-control']"))
time.sleep(1)

dropdown.select_by_visible_text("Female")
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'inlineRadio2']").click()
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[name = 'bday']").send_keys("02/02/2000")
time.sleep(1)

driver.execute_script("window.scrollTo(0,450)")
time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'btn btn-success']").click()
time.sleep(1)

driver.execute_script("window.scrollTo(0,120)")

# Success_message = (driver.find_element(by=By.CSS_SELECTOR,value="div[class = 'alert alert-success alert-dismissible']")).text
# print(Success_message)
# #Success_message = "Success! The Form has been submitted successfully!."
#
# assert Success_message == "Success! The Form has been submitted successfully!."
time.sleep(6)
driver.close()

