from appium import webdriver
import subprocess

subprocess.Popen('Appium', shell=True)


caps = {
    "platformName": "android",
    "appium:automationName": "UiAutomator2",
    "appium:uuid": "RZ8N82K8STY",
    "appium:deviceName": "Samsung Galaxy Note 20",
    "appium:appPackage": "com.jetpack.tesproject",
    "appium:appActivity": "com.jetpack.tesproject.MainActivity",
    "appium:noReset": True,
    "appium:fullReset": False,
    "appium:ignoreHiddenApiPolicyError": False,
    "appium:newCommandTimeout": 1000,
    "appium:enableMultiWindows": True,
    "disableIdLocatorAutocompletion": True,
}

driver = webdriver.Remote("http://127.0.0.1:4723", caps)
print(driver.is_app_installed('com.jetpack.tesproject'))
driver.start_activity('com.jetpack.tesproject', 'com.jetpack.tesproject.MainActivity')

#Locators
LOC_PURE_COMPOSE = 'composableUIButtonForComposableScreen'
LOC_CLASS = 'android.widget.TextView'
LOC_INSIDE_PURE_COMPOSE_IMAGE = 'composableImageView'
LOC_INSIDE_PURE_COMPOSE_IMAGE_TEXT = 'Zanzibar Photo'


if driver.find_element_by_id(LOC_PURE_COMPOSE).is_displayed():
    driver.find_element_by_id(LOC_PURE_COMPOSE).click()
    print("********** Clicked on PURE COMPOSE**********")
    print(" PURE COMPOSE IMAGE DISPLAYED -> ",driver.find_element_by_id(LOC_INSIDE_PURE_COMPOSE_IMAGE).is_displayed())

