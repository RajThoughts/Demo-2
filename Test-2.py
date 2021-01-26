from selenium import webdriver
from selenium.webdriver.support import select

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Raj")
driver.find_element_by_name("email").send_keys("Pani")
driver.find_element_by_css_selector("[placeholder='Password']").send_keys("Jaymatadi39")
driver.find_element_by_xpath("//[@id='exampleCheck1']").click()
# driver.find_element_by_class_name("alert-success").text
print(driver.find_element_by_class_name("alert-dismissible").text)
dropdown = select("")