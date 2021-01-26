from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
wait = WebDriverWait()
for obj in buttons:
    obj.click()
    driver.close()

