import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# Base class
# Define utilities here which are used across multiple test cases
# like logging, reporting, fixtures
# Also you can write common functions here like verifyLinkPresence(Just Pass Object and Text)
# eg. selectOptionByText, you can write control specific methods here/ general methods for
# each control
#

@pytest.mark.usefixtures("setup")  # 1 Add setup Fixture as this Fixture is common for each test case
# you can access methods of fixtures into BaseClass
class BaseClass:
# Logger Utility is used to create log along with inspect, file handler and Formatter
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text): # This method is used to verify that particular link is present or not
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):   # This method is used to select Gender
        sel = Select(locator)
        sel.select_by_visible_text(text)