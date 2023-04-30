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

driver = webdriver.Remote("http://0.0.0.0:4723", caps)
print(driver.is_app_installed('com.jetpack.tesproject'))
driver.start_activity('com.jetpack.tesproject', 'com.jetpack.tesproject.MainActivity')


#MIXED LOCATORS
LOC_MAIN_MIXED = 'composableUIButtonForMixedScreen'
LOC_MIXED_PURE_COMPOSE_IMAGE_VIEW = 'composableImageView'
LOC_INSIDE_MIXED_COMPOSE_TEXT_VIEW = 'composableTextView'
LOC_INSIDE_MIXED_COMPOSE_TEXT  = 'Pure Composable Design'

LOC_INSIDE_MIXED_XML_IMAGE_ID = 'com.jetpack.tesproject:id/xmlImageView'
LOC_ID_TEXT_VIEW ='com.jetpack.tesproject:id/xmlTextView'
LOC_INSIDE_MIXED_XML_TEXT = 'Pure XML Design'

in_user = int(input("Enter 1 for Compose 2 for mixed ui", ))


if driver.find_element_by_id(LOC_MAIN_MIXED).is_displayed():
    driver.find_element_by_id(LOC_MAIN_MIXED).click()
    print("********** Clicked on MIXED COMPOSE**********")
    if driver.find_element_by_id(LOC_MIXED_PURE_COMPOSE_IMAGE_VIEW).is_displayed():
        print(driver.find_element_by_id(LOC_INSIDE_MIXED_XML_IMAGE_ID).is_displayed())
        print("********** MIXED COMPOSE**********")
        print(driver.find_element_by_id(LOC_ID_TEXT_VIEW).text == LOC_INSIDE_MIXED_XML_TEXT)

        #PURE COMPOSE
        print("INDIE MIXED PURE COMPOSE TEXT VIEW -> ",driver.find_element_by_id(LOC_INSIDE_MIXED_COMPOSE_TEXT_VIEW).is_displayed())
    else:
        assert False
else:
    print("********** FAILED inside MIXED Screen**********")