**Description**
This is the PageObjectModel POM Model framework for Android Real device automation. The benefit of this framework is that, if the UI changes for the page, the tests themselves don’t need to change, only the code within the page object needs to change. 
Subsequently all changes to support that new UI are located in one place.

The Page Object Design Pattern provides the following advantages:
- There is a clean separation between test code and page specific code such as locators (or their use if you’re using a UI Map) and layout.
- There is a single repository for the services or operations offered by the page rather than having these services scattered throughout the tests

**Appium**
Appium is an open source test automation framework for use with native, hybrid and mobile web apps.
It drives iOS, Android, and Windows apps using the WebDriver protocol.

**Pre-Requisites**
Download, Install and Configure JDK
Download,  Install and Configure Appium Server
Download,  Install and Configure Python3
Download,  Install and Configure PyCharm IDE
Download,  Install and Configure Appium Python Client library
Download,  Install and Configure Selenium library
Download,  Install and Configure ADB for Android Automation
Download,  Install and Configure Pytest Lib in PyCharm IDE
Download,  Install and Configure Allure Reports Lib in PyCharm IDE

**Features**
Locator strategy
Screenshot on failure
Swipe feature for Page Scroll
Flick featue for Page Scroll
Allure report
Logger
Runner (Pytest)
MobileBy
Test script validation
pytest markers and orders
Handling NoElementfoudException and StaleElementFoundException


**Install python libraries**
pip3 install -r requirements.txt

**Test Runner**
Default:  pytest -m run

**Test Report**
Allure Report: 
pytest --alluredir=Reporting -m run
allure serve Reporting
                
