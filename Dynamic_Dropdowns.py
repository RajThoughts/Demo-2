import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(5)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
for country in countries:
    if country.text == "India":
        country.click()
        break
assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"


# driver.get("https://www.makemytrip.com/")
# driver.find_element_by_id("fromCity").click()
# driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
# time.sleep(2)
# cities =driver.find_elements_by_css_selector("p[class*='blackText']")
# print (len(cities))
# for city in cities:
#     if city.text =="Del Rio, United States":
#         city.click()
#         break
#
#
# driver.find_element_by_xpath("//p[text()='Delhi, India']").click()