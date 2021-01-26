import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

dropdown = Select(driver.find_element_by_xpath("//select[@id='exampleFormControlSelect1']"))
dropdown.select_by_index(1)
# or
dropdown.select_by_visible_text("Male")