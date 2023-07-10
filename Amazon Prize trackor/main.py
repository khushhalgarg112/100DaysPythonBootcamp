import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.facebook.com/")

driver.get(
    "https://www.amazon.in/Vivo-Starlit-Storage-Additional-Exchange/dp/B07WGPL7LV/?_encoding=UTF8&pd_rd_w=yypwV&content-id=amzn1.sym.0f264ee2-aac7-4fdc-9e2f-805839060ce8&pf_rd_p=0f264ee2-aac7-4fdc-9e2f-805839060ce8&pf_rd_r=Q80P1MVX8DNS4RJ0D2GV&pd_rd_wg=lrWpD&pd_rd_r=90b737f6-bdf9-4ddf-b15e-59b01345270b&ref_=pd_gw_deals_4s_t1&th=1"
)

# price = driver.find_element(By.CLASS_NAME, "_8eso")
# print(price.text)

write = driver.find_element(
    By.XPATH,
    '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]',
)

price = write.text.split(",")
new_price = ""
for element in price:
    new_price = new_price + element

final = int(new_price)

driver.quit()

EMAIL = "khusgarg1@gmail.com"
PASSWORD = "katyhecfyjtevspe"

smtp_server = "smtp.gmail.com"
smtp_port = 587

if final < 15000:
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="khusgarg2002@gmail.com",
            msg=f"Your Product is not below {final}\n Buy Now-> https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/ref=sr_1_1_sspa?crid=1ALBV3RQCTFUY&keywords=boat&qid=1688908275&sprefix=boa%2Caps%2C489&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        )
