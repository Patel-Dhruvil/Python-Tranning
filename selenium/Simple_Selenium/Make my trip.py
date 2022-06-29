import time
from selenium import webdriver
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import xlwt
from xlwt import Workbook
wb = Workbook()

driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()


driver.find_element(by=By.CSS_SELECTOR,value="span[class = 'langCardClose']").click()
driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'fromCity']").click()
time.sleep(2)
driver.find_element(by=By.CSS_SELECTOR,value="div[role = 'combobox'] input").send_keys("surat")
time.sleep(4)
dropdown = (driver.find_elements(by=By.CSS_SELECTOR,value="div[class = 'calc60'] p"))
for i in dropdown:
    if i.text in "Surat, India":
        i.click()
        break
time.sleep(2)

dropdown = (driver.find_elements(by=By.CSS_SELECTOR,value="div[class = 'calc60'] p"))
for i in dropdown:
    if i.text == "Pune, India":
        i.click()
        break
time.sleep(2)

next_button = driver.find_element(by=By.CSS_SELECTOR,value="span[class = 'DayPicker-NavButton DayPicker-NavButton--next']")

Current_Month = date.today().month
Current_date = date.today().day
Departure_Month = 9
Departure_Date = 28
Return_Month = 9
Return_Date = 29
i = 0
if Current_Month > Departure_Month:
    i = int((12-Current_Month) + Departure_Month)
else:
    i = int(Departure_Month - Current_Month)
for next in range(i):
    next_button.click()
Current_Month = int(Current_Month + i)
print(Current_Month)
time.sleep(3)
driver.execute_script("window.scrollTo(0,130)")
SelectDate = (driver.find_elements(by=By.CSS_SELECTOR,value="div[aria-disabled = 'false'] p"))  #div[class = 'DayPicker-Body'] p
print(Current_date)
print(Departure_Date)
if Current_date <= Departure_Date:
    for ii in SelectDate:
        #print(ii.text)
        if int(ii.text) == Departure_Date:
            #print("in the loop of date")
            #print(ii.text)
            ii.click()
            break
else:
    print("Please select valid date")

time.sleep(2)
# for return date
driver.find_element(by=By.XPATH,value="//*[@id='root']/div/div[2]/div/div/div[2]/div[1]/div[4]").click()
next_button = driver.find_element(by=By.CSS_SELECTOR,value="span[class = 'DayPicker-NavButton DayPicker-NavButton--next']")
time.sleep(2)
i = 0#problem
if Current_Month == Return_Month:
    i = 0
elif Current_Month > Return_Month:
    i = int((12-Current_Month) + Return_Month)
    print(i)
else:
    i = int(Return_Month - Current_Month)
    print(i)
for next in range(i):
    next_button.click()

time.sleep(5)

SelectDate = (driver.find_elements(by=By.CSS_SELECTOR,value="div[aria-disabled = 'false'] p"))
print(Current_date)
print(Return_Date)
if Current_date <= Return_Date:
    for ii in SelectDate:
        if int(ii.text) == Return_Date:
            ii.click()
            break
else:
    print("Please select valid date")
time.sleep(2)
driver.find_element(by=By.CSS_SELECTOR,value="div[class = 'widgetSection appendBottom40 primaryTraveler '] p a").click()
flightData = []
Flights = driver.find_elements(by=By.CSS_SELECTOR,value="div[class = 'listingCardWrap'] div div[class = 'listingCard ']")
print(Flights)
for flight in Flights:
    flightData.append(str(flight.text))
sheet1 = wb.add_sheet('Sheet 1')

for iii in range(len(Flights)):
    print(flightData[iii])

    sheet1.write(iii,0,flightData[iii])

wb.save('flightData.xls')

print("-------------------------------")#print(flightData[0])

# for visibal month div[class = 'DayPicker-Caption'] div
# for date div[class = 'DayPicker-Body'] p
time.sleep(2)
sure = driver.find_element(by=By.CSS_SELECTOR,value="div[class = 'hsw_inputBox width160'] input[id = 'fromCity']")
Sure = driver.find_element(by=By.CSS_SELECTOR,value="input[id = 'toCity']")
print(sure.get_attribute("value"))
print(Sure.get_attribute("value"))

assert "Surat, India" == sure.get_attribute("value")
assert "Pune, India" == Sure.get_attribute("value")

#radio = driver.find_elements(by=By.CSS_SELECTOR,value="div[class = ' flightsContainer makeFlex hrtlCenter'] ul li span[class = 'radioSelect']")

# try:
#     for i in radio:
#         i.click()
#         time.sleep(1)
#     time.sleep(8)
# except:
#     print("Error happend durind click")

driver.close()