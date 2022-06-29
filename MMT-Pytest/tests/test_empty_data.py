import time
from datetime import date
from selenium.webdriver.common.by import By
from pageObjects.MMTHomePage import MMTHomePage
from utilities.BaseClass import BaseClass

class TestHomePage001(BaseClass):
#second test with return date empty.
    def test_ReturnDateEmpty(self):

        log = self.getLogger()
        homepage = MMTHomePage(self.driver)
        log.info("Start the Valid test ")
        #homepage.getName().send_keys(getData["firstname"])--------example
        time.sleep(2)
        homepage.ClosePopup().click()
        time.sleep(2)
        homepage.FromCity().click()
        time.sleep(2)
        homepage.FromCityInput().send_keys("surat")
        time.sleep(2)
        dropdown = homepage.CityDropdown()
        for i in dropdown:
            if i.text in "Surat, India":
                i.click()
                break
        log.info("Selected the city surat")
        time.sleep(2)

        dropdown = homepage.CityDropdown()
        for i in dropdown:
            if i.text == "Pune, India":
                i.click()
                break
        log.info("Selected the city Pune")
        time.sleep(2)

        next_button = homepage.NextMonthButton()

        Current_Month = date.today().month
        Current_date = date.today().day
        Departure_Month = 9
        Departure_Date = 29
        i = 0
        if Current_Month > Departure_Month:
            i = int((12 - Current_Month) + Departure_Month)
        else:
            i = int(Departure_Month - Current_Month)
        for next in range(i):
            next_button.click()
        log.info("Selected the Departure Month")
        Current_Month = int(Current_Month + i)
        print(Current_Month)
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0,130)")

        SelectDate = homepage.SelectVisibleDate()

        if Current_date <= Departure_Date:
            for ii in SelectDate:
                # print(ii.text)
                if int(ii.text) == Departure_Date:
                    # print("in the loop of date")
                    print(ii.text)
                    ii.click()
                    break
        else:
            print("Please select valid date")
        log.info("Selected the Departure Date")
        homepage.SubmitButton().click()


        log.info(f"Completed Ticket booking for {Departure_Date}/{Departure_Month}")
