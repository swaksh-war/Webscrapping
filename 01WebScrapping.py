from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
import time

driver=webdriver.Chrome("C:\ProgramData\chromedriver.exe")
driver.get("https://myanimelist.net/login.php?from=%2F")

username=driver.find_element_by_id("loginUserName")
username.send_keys("Capti")
password=driver.find_element_by_id("login-password")
password.send_keys("SandyRuby@12")

password.send_keys(Keys.ENTER)

with open("malhomepage.html") as f:
    f.write(driver.page_source)

mylist=driver.find_element_by_tag_name()
TouchActions.tap()

time.sleep(12)
driver.quit()