from appium import webdriver as wd
from appium.webdriver.common.touch_action import TouchAction



Desired_cap = {
    "platformName": "android",
    "uuid": "RZ8N82K8STY",
    "deviceName": "Samsung Galaxy Note 20",
    # "appPackage": "com.android.Mobile_appiumflags",
    # "appActivity": "com.tivo.android.screens.setup.SplashActivity",
    "app": "/Users/hakumar/PycharmProjects/Experiments/Mobile_appium/app_installation_files/app-debug.apk",
    "noReset": True,
    "fullReset": False,
    "ignoreHiddenApiPolicyError": False,
    "newCommandTimeout": 1000,
}

from_ = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx" \
                ".compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view." \
                "View[2]/android.view.View[14]"
destination_Brunie_flag = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget." \
                          "FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/" \
                          "android.view.View/android.view.View[2]/android.view.View[13]"
dest_final_ele = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/" \
                 "androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/" \
                 "android.view.View[2]/android.view.View[11]/android.view.View"
driver = wd.Remote("http://localhost:4723/wd/hub", Desired_cap)

last_cn_name = 'Dominica'

driver.implicitly_wait(5)

to_ = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx." \
          "compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.view." \
          "View[2]/android.view.View[2]"

driver.implicitly_wait(4)
start_x=driver.get_window_size()['width']
start_y=driver.get_window_size()['height']
print(f'Starting {start_x} and {start_y} screen width and hieght')

s_x=driver.find_element_by_xpath(from_).location['x']
s_y=driver.find_element_by_xpath(from_).location['y']
print(f'Starting {s_x} and {s_y} start location values')

end_x=driver.find_element_by_xpath(to_).location['x']
end_y=driver.find_element_by_xpath(to_).location['y']
print(f'Starting {end_x} and {end_y} end location values')

#driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new uiselector().resourceid(elementId).instance(0));')

c=0
for i in range(0,24):
    if(driver.find_element_by_xpath(destination_Brunie_flag).is_displayed()):
        print("Find it")
        c = c + 1
        driver.swipe(s_x, s_y, end_x, end_y, 2000)
        print('Count = ', c)
        if c == 21:
            driver.find_element_by_xpath(dest_final_ele).is_displayed()
            break

cn_name = 'Brunei'
brunie_loc = ''
for m in range(1,15):
    cn_name = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                           "android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/"
                                           "android.view.View/android.view.View/"
                                           "android.view.View/android.view.View[2]/"
                                           "android.view.View[{}]".format(m)).text
    print("Country lists are :", country_key_val, '\n')
