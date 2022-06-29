import pytest
from selenium import webdriver
import time

driver = None  # Declare Driver object Globally


def pytest_addoption(parser):   # 3 Please refer https://docs.pytest.org/en/latest/example/simple.html
                                # command line parameter default is chrome
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")  # 1 Add Fixture which are common for each test Cases
def setup(request):  # 2 Browser invoke Code is written here
    global driver # Use Global Driver so everytime it will not be created newly
    browser_name = request.config.getoption("browser_name")    # 4 Get/ Retrieve the value of Browser from command line
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\selenium_driver\\chromedriver.exe")

    driver.get("http://demowebshop.tricentis.com/")  # Application Url
    driver.maximize_window()

    request.cls.driver = driver  # Local Driver - which will be used to pass driver automatically
    # to each class to access class variables we used Self this is used to pass
    yield
    driver.close()

# Custom Report Code, Dont go into the details, Copy Paste theSame in each Project pytest_runtest_makereport
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

# Screenshot Capture Function - Selenium
def _capture_screenshot(name):
     driver.get_screenshot_as_file(name)
