from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

email = input("enter the email id?: ")
password = input("enter the password?: ")

driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")
driver.get("https://accounts.google.com/AddSession?sacu=1&service=lso#identifier")

driver.find_element_by_id("Email").send_keys(email)
driver.implicitly_wait(1)
driver.find_element_by_id("next").click()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@id='Passwd']").send_keys(password)
driver.implicitly_wait(1)
driver.find_element_by_id("signIn").click()
driver.execute_script("window.open('https://mail.google.com/mail/u/0/#inbox','New Window')")
driver.implicitly_wait(1)
