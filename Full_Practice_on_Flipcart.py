from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("raj.kajalpani")
driver.find_element_by_id("pass").send_keys("JAYMATADI39")

