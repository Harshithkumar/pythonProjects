from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.ebay.com')
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='gh-shop-a']").click()  # shop by category drop down
driver.find_element_by_xpath(
    "//*[@href='https://www.ebay.com/b/Cell-Phones-Smart-Watches-Accessories/15032/bn_1865441']").click()#undercat
driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div/div/div/section/ul/li[3]/a").click() #cellphones
driver.find_element_by_xpath("/html/body/div[4]/div[4]/div[3]/div[1]/section[1]/div[1]/div[2]/button/span[1]").click()#sellAll
driver.implicitly_wait(3)
driver.find_element_by_xpath("/html/body/div[13]/div[2]/div/form/div[1]/div[1]/div/div[8]/span").click()#Screensize
screen_size_value_count = driver.find_elements_by_xpath("//div/fieldset/div[1]/div")
print("Count = ", len(screen_size_value_count))

for i in screen_size_value_count:
    print("screen_size_value_count = ", i.text)
screen_size_value_count[2].click()