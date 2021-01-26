from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r"D:\New Applications 2020\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Raj")
driver.find_element_by_name("email").send_keys("saskesfriends@gmail.com")
driver.find_element_by_css_selector("[placeholder = 'Password']").send_keys("Raj")
driver.find_element_by_id("exampleCheck1").click()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(1)
# driver.refresh()
