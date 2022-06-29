import time
from datetime import date
from selenium.webdriver.common.by import By
from pageObjects.MMTHomePage import MMTHomePage
from utilities.BaseClass import BaseClass
import xlwt
from xlwt import Workbook



class TestHomePage(BaseClass):

    def test_TicketBook(self):
        wb = Workbook()
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
        Return_Month = 10
        Return_Date = 29
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
        time.sleep(5)
        # for return date-------------------------------------------
        print("in return date")
        print(homepage.ToCityButton())
        homepage.ToCityButton().click()
        print("for return date")
        time.sleep(2)
        next_button = homepage.NextMonthButton()

        i = 0  # problem
        if Current_Month == Return_Month:
            i = 0
        elif Current_Month > Return_Month:
            i = int((12 - Current_Month) + Return_Month)
            print(i)
        else:
            i = int(Return_Month - Current_Month)
            print(i)
        for next in range(i):
            print(i)
            next_button.click()
        log.info("Selected the Return Month")

        time.sleep(5)
        SelectDate = homepage.SelectVisibleDate()
        if Current_date <= Return_Date:
            for ii in SelectDate:
                if int(ii.text) == Return_Date:
                    ii.click()
                    print(ii)
                    break
        else:
            print("Please select valid date")
        time.sleep(5)
        log.info("Selected the Return Date")

        homepage.SubmitButton().click()
        log.info(f"Completed Ticket booking for {Departure_Date}/{Departure_Month} to {Return_Date}/{Return_Month}")

        flightData = []
        Flights = self.driver.find_elements(by=By.CSS_SELECTOR,
                                       value="div[class = 'listingCardWrap'] div div[class = 'listingCard ']")
        print(Flights)
        for flight in Flights:
            flightData.append(str(flight.text))
        sheet1 = wb.add_sheet('Sheet 1')

        for iii in range(len(Flights)):
            print(flightData[iii])

            sheet1.write(iii, 0, flightData[iii])

        # TDate = date.today().strftime("%d/%m/%Y")
        # filename = f'flightData_{ TDate}'
        wb.save('filename.xls')
        sure = homepage.ConfirmFromCity().get_attribute("value")
        Sure = homepage.ConfirmToCity().get_attribute("value")
        Depart = homepage.ConfirmDepartDate().get_attribute("value")
        Return = homepage.ConfirmReturnDate().get_attribute("value")
        print(sure)
        print(Sure)

        assert "Surat, India" == sure,"data not match"
        assert "Pune, India" == Sure,"data not match"
        #assert "Tue, Sep 27, 2022" == Depart,"data not match"
        #assert "Fri, Oct 28, 2022" == Return,"data not match"


    # @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    # def getData(self, request):
    #     return request.param

