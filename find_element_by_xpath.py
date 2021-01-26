from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# driver.find_element_by_xpath("//input[@type='text']").send_keys("Lipu")
driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']").send_keys("Rocky")