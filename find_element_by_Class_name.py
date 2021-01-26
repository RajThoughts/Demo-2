from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.find_element_by_class_name("alert-dismissible").text)