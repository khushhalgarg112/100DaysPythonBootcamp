from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.facebook.com/")

email = driver.find_element(By.NAME, "email")
email.send_keys("XXXXXXX@gmail.com")

password = driver.find_element(By.NAME, "pass")
password.send_keys("XXXXXXXX")

login = driver.find_element(By.NAME, "login")
login.click()