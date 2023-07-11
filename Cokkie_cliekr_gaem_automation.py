# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# chrome_driver_path = "C:\development\chromedriver.exe"

# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Cookie = driver.find_element(By.ID, "cookie")

# score = driver.find_element(By.ID, "money")
# score_value = int(score.text)

# cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
# click_cursor = driver.find_element(By.ID, "buyCursor")
# get_cursor = int(cursor.text.split("-")[1])

# while True:
#     Cookie.click()
#     if get_cursor > score_value:
#         click_cursor.click()
#         Cookie.click()
#     else:
#         Cookie.click()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

#Get upgrade item ids.
items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    cookie.click()

    # if time.time() > timeout:
    #     items_prize = driver.find_elements(By.CSS_SELECTOR, "#store b")
    #     prizes = []

    #     for item in items_prize:
    #         prizes.append(int(item.text.split("-")[1].strip().replace(",", "")))

    #     id_and_prices = {}

    #     for n in range(len(prizes)):
    #         id_and_prices[prizes[n]] = item_ids[n]

    #     score = driver.find_element(By.ID, "money")
    #     if "," in score:
    #        score = score.replace(",", "")
    #     total_score = int(score.text)

    #     print(total_score)

    #     print(id_and_prices)


    #Every 5 seconds:
    if time.time() > timeout:

        #Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR,"#store b")
        item_prices = []

        #Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element(By.ID,"money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID,to_purchase_id).click()
        
        #Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break
