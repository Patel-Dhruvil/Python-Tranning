import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.maximize_window()

radio = driver.find_elements(by=By.CSS_SELECTOR,value="input[class = 'radioButton']")
for i in radio:
    i.click()
    time.sleep(1)

driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'inputs ui-autocomplete-input']").send_keys("india")

select = len(driver.find_elements(by=By.TAG_NAME,value="option"))
for i in range(1,select):
    driver.find_element(by=By.CSS_SELECTOR, value=f"option[value = 'option{i}'").click()
    time.sleep(1)

checkbox = len(driver.find_elements(by=By.CSS_SELECTOR,value="div[class = 'checkbox-example']"))
print(checkbox)
for i in range(1,checkbox):
    driver.find_element(by=By.CSS_SELECTOR, value=f"option[value = 'option{i}'").click()
    time.sleep(1)

for i in range(1,4):
    driver.find_element(by=By.CSS_SELECTOR,value=f"input[id = 'checkBoxOption{i}']").click()
    time.sleep(1)

# -------------------------------------swich the window of browser.---------------------------------------------------
driver.find_element(by=By.XPATH,value="//button[text() = 'Open Window']").click()
time.sleep(5)
#mainWindow = driver.window_handles[0]
driver.switch_to.window(driver.window_handles[0])

# -------------------------------------swich the tab of window.----------------------------------------------------
driver.find_element(by=By.CSS_SELECTOR,value="a[class = 'btn-style class1 class2']").click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])

# ------------------------------------Alert box and confirm box -----------------------------------------------------
driver.find_element(by=By.CSS_SELECTOR,value="input[class = 'inputs']").send_keys("Dhruvil")
driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'alertbtn']").click()
time.sleep(1)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'confirmbtn']").click()
time.sleep(1)
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()

#--------------------------------------take a data form table ---------------------------------------------------
table = driver.find_element(by=By.CSS_SELECTOR,value="table[id = 'product']").text
print(table)

#----------------------------------------hide and show ------------------------------------------------------------
driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'displayed-text']").send_keys("Dhruvil")
time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'hide-textbox']").click()
time.sleep(1)
driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'show-textbox']").click()

aaa = driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'displayed-text']")

assert driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'displayed-text']") == driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'displayed-text']")


#---------------------------------------------Mouse hover --------------------------------------------------------------
# a = ActionChains(driver)
# time.sleep(1)
# m = driver.find_element(by=By.CSS_SELECTOR, value="button[id='mousehover']")
# a.move_to_element(m).perform()
# time.sleep(1)
# n = driver.find_element(by=By.XPATH, value="//a[text()='Top']")
# a.move_to_element(n).click().perform()

time.sleep(1)
(ActionChains(driver)).move_to_element(driver.find_element(by=By.CSS_SELECTOR, value="button[id='mousehover']")).perform()
time.sleep(1)
(ActionChains(driver)).move_to_element(driver.find_element(by=By.XPATH, value="//a[text()='Top']")).click().perform()













time.sleep(8)
driver.close()
driver.quit()

