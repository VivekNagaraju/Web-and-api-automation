from selenium import webdriver
from selenium.webdriver.common.by import By

'''1. launching the chrome browser with detach option and maximising the window'''
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.maximize_window()
# driver.implicitly_wait(10)

'''2. Navigating to target URL'''
driver.get("https://testautomationpractice.blogspot.com/")

'''3. Enter Name'''
# driver.find_element(By.ID, "name").send_keys("Vivek") # not recommended
name_txtbx=driver.find_element(By.XPATH, "//input")
name_txtbx.send_keys("Vivek")

'''4. Enter email'''
email_txtbx=driver.find_element(By.XPATH, "//input[@id='email']")
email_txtbx.send_keys("vivek@gmail.com")
