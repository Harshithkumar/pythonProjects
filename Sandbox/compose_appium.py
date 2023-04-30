from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

caps = {}
caps["platformName"] = "android"
caps["appium:automationName"] = "UiAutomator2"
caps["appium:uuid"] = "RZ8N82K8STY"
caps["appium:deviceName"] = "Samsung Galaxy Note 20"
caps["appium:appPackage"] = "com.example.jetpackcomposeplayground"
caps["appium:appActivity"] = "com.example.jetpackcompose.core.MainActivity"
caps["appium:noReset"] = True
caps["appium:fullReset"] = False
caps["appium:ignoreHiddenApiPolicyError"] = False
caps["appium:newCommandTimeout"] = 1000
caps["appium:enableMultiWindows"] = True

driver = webdriver.Remote("http://0.0.0.0:4723", caps)
print(driver.is_app_installed('com.example.jetpackcomposeplayground'))
driver.start_activity('com.example.jetpackcomposeplayground', 'com.example.jetpackcompose.core.MainActivity')
LOC_DISPLAY_STYLED_TEXT = 'com.example.jetpackcomposeplayground:id/custom_text_example'
LOC_Clickable_Component = 'com.example.jetpackcomposeplayground:id/load_clickable_example'
LOC_INSIDE_STYLED_TEXT = '/hierarchy/android.widget.FrameLayout[2]/android.widget.LinearLayout/' \
                         'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/' \
                         'android.view.ViewGroup/android.view.View/android.widget.ScrollView/android.view.View[6]'
LOC_Click_Dialog_btn = '//*[@text="Click to see dialog"]'
LOC_xpath_Click_Dialog_btn = '//android.view.View[@content-desc="desc"]'
LOC_Final_dailog  ='/hierarchy/android.widget.FrameLayout[2]/android.widget.FrameLayout/' \
 'android.widget.FrameLayout/android.view.ViewGroup/android.view.View/' \
 'android.view.View/android.view.View/android.view.View[2]/android.view.View'

# if driver.find_element_by_id(LOC_DISPLAY_STYLED_TEXT).is_displayed():
#     driver.find_element_by_id(LOC_DISPLAY_STYLED_TEXT).click()
#     print("********** Clicked**********")
#     if driver.find_element_by_xpath(LOC_INSIDE_STYLED_TEXT).is_displayed():
#         print("********** STYLE TEXT is Present **********")


if driver.find_element_by_id(LOC_Clickable_Component).is_displayed():
    driver.find_element_by_id(LOC_Clickable_Component).click()
    print("********** Clicked**********")
    #driver.update_settings({'disableIdLocatorAutocompletion': True})
    driver.implicitly_wait(3)
    if driver.find_element_by_xpath(LOC_xpath_Click_Dialog_btn).is_displayed():
        driver.find_element_by_xpath(LOC_xpath_Click_Dialog_btn).click()
        print("********** STYLE TEXT is Present **********")
