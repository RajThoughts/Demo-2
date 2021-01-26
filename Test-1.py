from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.facebook.com/")
driver.find_element_by_css_selector("input[aria-label = 'Email address or phone number']").send_keys("raj.kajalpani")
driver.find_element_by_xpath("//input[@placeholder = 'Password']").send_keys("bharati@2019")
driver.find_element_by_name("login").click()


