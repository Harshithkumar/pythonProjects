import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_find_index_list():
    global country_key_val
    LOC_XPATH_CN_CODE = "//*[@id='country_code']/option"
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://accounts.lambdatest.com/register")
    driver.implicitly_wait(2)
    print("Website Loaded")
    driver.find_element_by_xpath("//*[@id='country_code']").click()
    CN_CODE_List = driver.find_elements_by_xpath(LOC_XPATH_CN_CODE)
    print("Len of the country list ", len(CN_CODE_List))


    # this use list method to capture the country code
    # for i in range(1, len(CN_CODE_List)):
    #     country_list = driver.find_element_by_xpath("//*[@id='country_code']/option[{}]".format(i)).text
    #     print("Country lists are :", country_list,'\n')

    # county_name = driver.find_element_by_xpath("//*[@id='country_code']/option[{}]".format(76)).text
    # driver.find_element_by_xpath("//*[@id='country_code']/option[{}]".format(76)).click()
    # print(county_name, ': is clicked')


    # this use hash map  method to capture the country code
    country_key_val = {}
    for j in range(2, len(CN_CODE_List)):
        country_key_val[j] = driver.find_element_by_xpath("//*[@id='country_code']/option[{}]".format(j)).text
        print("Country lists are :", country_key_val, '\n')

    print("***********************KEYS******************************")
    cn_code = list(country_key_val.keys())[list(country_key_val.values()).index('Algeria (+213)')]
    print("key cn code :",int(cn_code))


    print("***********************VALUES******************************")
    cn_val = list(country_key_val.values())[list(country_key_val.keys()).index(4)]
    print("cn value name is :",cn_val)

    cn_name = driver.find_element_by_xpath("//*[@id='country_code']/option[{}]".format(cn_code)).text
    driver.find_element_by_xpath("//*[@id='country_code']/option[{}]".format(cn_code)).click()
    assert cn_name == 'Algeria (+213)'