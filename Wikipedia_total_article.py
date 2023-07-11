from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

no_of_article = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(no_of_article.text)

driver.quit()
