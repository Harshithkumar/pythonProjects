import os
from appium import webdriver
import re
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from appium.webdriver.connectiontype import ConnectionType
from self import self

from tools.ssh_sys_commands import SSH_Commands
from appium.webdriver.mobilecommand import MobileCommand as Command

Desired_cap = {
    "platformName": "android",
    "uuid": "RZ8N82K8STY",
    "deviceName": "Samsung Galaxy Note 20",
    "appPackage": "com.tivo.cableco",
    "appActivity": "com.tivo.android.screens.setup.SplashActivity",
    "noReset": True,
    "ignoreHiddenApiPolicyError": False,
    "newCommandTimeout": 1000,
}

# attribute = {}
driver = webdriver.Remote("http://localhost:4723/wd/hub", Desired_cap)
driver.implicitly_wait(11000)
print(driver.find_element_by_id("com.tivo.cableco:id/tivoCastButton").is_displayed())
cast_location = driver.find_element_by_id("com.tivo.cableco:id/tivoCastButton").location

cast_location_bound = driver.find_element_by_id("com.tivo.cableco:id/tivoCastButton").get_attribute('bounds')

search_position_location = driver.find_element_by_id('com.tivo.cableco:id/menu_item_search').location

search_position_bound_value = driver.find_element_by_id('com.tivo.cableco:id/menu_item_search').get_attribute('bounds')

print("Cast Location = ", cast_location)

print("Cast Location bound value = ", cast_location_bound, type(cast_location_bound))

print("Search Position Location = ", search_position_location)

print("Search Position Bound value = ", search_position_bound_value)

casticon_X = cast_location.get('x')
casticon_Y = cast_location.get('y')

parent_bound_value = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                    'android.widget.FrameLayout/android.view.ViewGroup/android.widget.'
                                                    'FrameLayout[1]/android.view.ViewGroup/androidx.appcompat.widget.'
                                                    'LinearLayoutCompat').get_attribute('bounds')

Cast_icon_coordinate = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
                                                    'android.widget.FrameLayout/android.view.ViewGroup/android.widget.'
                                                    'FrameLayout[1]/android.view.ViewGroup/androidx.appcompat.widget.'
                                                    'LinearLayoutCompat').location
print("parent_bound_value = ", parent_bound_value)

print("Cast_icon_coordinate value = ", Cast_icon_coordinate, type(Cast_icon_coordinate))
print("Contains or not = ", Cast_icon_coordinate.__contains__(str(cast_location.get('x'))))

X_co_ordinate_parent = Cast_icon_coordinate.get('x')
Y_co_ordinate_parent = Cast_icon_coordinate.get('y')
print("Parent coordinatees", X_co_ordinate_parent, Y_co_ordinate_parent)
print("Child coordinatees", casticon_X, casticon_Y)

if casticon_X <= X_co_ordinate_parent and casticon_Y <= Y_co_ordinate_parent:
    print("Cast icon is present in the same coordinates as designed")







#
# def switch_to_mobile_data(value):
#         result  = driver.execute_script('mobile: shell', {
#                 'command': 'svc data',
#                 'args': [value],
#                 # 'includeStderr': True,
#                 # 'timeout': 5000
#         })
#         #assert value == 'disable', "Mobile data is not ON !! "
#         print("hello -> ", result)

#
# # driver.set_network_connection(ConnectionType.DATA_ONLY)
# switch_to_mobile_data(value = 'enable')


#
# switch_to_mobile_data(value='enable')
# driver.start_session(Desired_cap)
# time.sleep(10)
# driver.find_element_by_xpath().is_displayed()
# driver.swipe(100, 100, 100, 400, 5000)
