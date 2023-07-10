from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

"""driver.get("https://www.facebook.com/")
price = driver.find_element(By.CLASS_NAME, "_8eso")
print(price.text)"""

"""driver.get("https://www.amazon.in/Vivo-Starlit-Storage-Additional-Exchange/dp/B07WGPL7LV/?_encoding=UTF8&pd_rd_w=yypwV&content-id=amzn1.sym.0f264ee2-aac7-4fdc-9e2f-805839060ce8&pf_rd_p=0f264ee2-aac7-4fdc-9e2f-805839060ce8&pf_rd_r=Q80P1MVX8DNS4RJ0D2GV&pd_rd_wg=lrWpD&pd_rd_r=90b737f6-bdf9-4ddf-b15e-59b01345270b&ref_=pd_gw_deals_4s_t1&th=1")
write = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
price = write.text.split(",")
new_price = ""
for element in price:
    new_price = new_price + element

final = int(new_price)
print(type(final))"""

# driver.close()  # This close only one tab
# driver.quit()  # this close all the tabs open into the browser

driver.get("https://www.python.org/")

dic = {
    "time": "",
    "name": "",
}

final = {}
i = 1
times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
texts = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": texts[n].text
    }

print(events)
    
driver.quit()