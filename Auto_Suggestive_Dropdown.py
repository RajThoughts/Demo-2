from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")

countries = driver.find_element_by_xpath("//li[@class='ui-menu-item']/a")
# print(len(Countries))
for country in countries:
    assert isinstance(country.text, object)
    country.text
    country.click()
    break
# assert driver.find_element_by_css_selector("li[role = 'presentation'] a") == "india"