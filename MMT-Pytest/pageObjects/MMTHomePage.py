from selenium.webdriver.common.by import By


class MMTHomePage:

    def __init__(self, driver):
        self.driver = driver

    # example = name = (By.CSS_SELECTOR, "[name='name']")---------------
    Popup_close = (By.CSS_SELECTOR,"span[class = 'langCardClose']")
    From_City = (By.CSS_SELECTOR,"input[id = 'fromCity']")
    From_City_Input = (By.CSS_SELECTOR,"div[role = 'combobox'] input")
    City_Dropdown = (By.CSS_SELECTOR,"div[class = 'calc60'] p")
    Next_Month_Button = (By.CSS_SELECTOR,"span[class = 'DayPicker-NavButton DayPicker-NavButton--next']")
    Select_visible_Date = (By.CSS_SELECTOR,"div[aria-disabled = 'false'] p")
    To_City_Button = (By.CSS_SELECTOR,"body.desktop.in.webp:nth-child(2) div.bgGradient.webpSupport div.minContainer div:nth-child(1) div.widgetSection.appendBottom40.primaryTraveler div.fsw div.fsw_inner.returnPersuasion:nth-child(1) > div.fsw_inputBox.dates.reDates.inactiveWidget:nth-child(5)")
    Submit_Button = (By.CSS_SELECTOR,"div[class = 'widgetSection appendBottom40 primaryTraveler '] p a")
    Confirm_From_City = (By.CSS_SELECTOR,"div[class = 'hsw_inputBox width160'] input[id = 'fromCity']")
    Confirm_To_City = (By.CSS_SELECTOR,"input[id = 'toCity']")
    Confirm_Depart_Date = (By.CSS_SELECTOR,"input[id = 'departure']")
    Confirm_Return_Date = (By.CSS_SELECTOR,"input[id = 'return']")
    # def getName(self):
    #     return self.driver.find_element(*HomePage.name)   Example--------------
    def ClosePopup(self):
        return self.driver.find_element(*MMTHomePage.Popup_close)

    def FromCity(self):
        return self.driver.find_element(*MMTHomePage.From_City)

    def FromCityInput(self):
        return self.driver.find_element(*MMTHomePage.From_City_Input)

    def CityDropdown(self):
        return self.driver.find_elements(*MMTHomePage.City_Dropdown)

    def NextMonthButton(self):
        return self.driver.find_element(*MMTHomePage.Next_Month_Button)

    def SelectVisibleDate(self):
        return self.driver.find_elements(*MMTHomePage.Select_visible_Date)

    def ToCityButton(self):
        return self.driver.find_element(*MMTHomePage.To_City_Button)

    def SubmitButton(self):
        return self.driver.find_element(*MMTHomePage.Submit_Button)

    def ConfirmFromCity(self):
        return self.driver.find_element(*MMTHomePage.Confirm_From_City)

    def ConfirmToCity(self):
        return self.driver.find_element(*MMTHomePage.Confirm_To_City)

    def ConfirmDepartDate(self):
        return self.driver.find_element(*MMTHomePage.Confirm_Depart_Date)

    def ConfirmReturnDate(self):
        return self.driver.find_element(*MMTHomePage.Confirm_Return_Date)












